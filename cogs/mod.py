import discord
from discord import guild
from discord.errors import HTTPException
from discord.ext import commands
from discord import User
import datetime
import typing
from datetime import datetime
import asyncio
import re

from discord.ext.commands.core import check


class Mod(commands.Cog, name='Mod'):

    def __init__(self,bot):
        self.bot = bot

#nick CMD

    @commands.command()
    @commands.has_permissions(manage_nicknames=True)
    async def nick(self, ctx, member: discord.Member, *, nick):
        if ctx.guild.me.top_role < member.top_role:
            return await ctx.send(f"**<a:RedTick:796628786102927390> This Member has A Greater Role Than Me...**")
        if ctx.message.author.top_role <= member.top_role:
            return await ctx.send(f"**<a:RedTick:796628786102927390> You can't change nick of that person**")
        else:
            await member.edit(nick=nick)
            await ctx.send(f'```{member} nickname was changed to {nick} by {ctx.message.author}```')

#kick CMD

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, user : discord.Member, *, reason = None):
        """Kicks a user from the server."""
        if user == ctx.guild.owner:
            return await ctx.send(f'**<a:RedTick:796628786102927390> You are not cool enough to kick that person.**')
        if ctx.author == user:
            await ctx.send("You cannot kick yourself.")
            return
        if ctx.message.author.top_role <= user.top_role:
            await ctx.send(f"**<a:RedTick:796628786102927390> You are not cool enough to kick that person.**")
            return
        if user.id == self.bot.owner_id:
            await ctx.send(f"**<:smile_yay:849338019306668052> You can ask my Owner to Leave The Server, He will do it himself!**")
            return
        else:
            await user.kick()
            kick_msg = f"``` You have been kicked from {ctx.guild.name} for {reason} by the Moderator - {ctx.author.name}```"
            kick_embed = discord.Embed(description=f'**<:verifiedserver:796628753005543444> ``{user}`` was successfully kicked!**', color=0x3498DB)
            await ctx.send(embed=kick_embed)
            await user.send(kick_msg)

#ban CMD

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, user : typing.Union[discord.User, discord.Member], *, reason =None):
        guild = ctx.guild
        if user == ctx.guild.owner:
            return await ctx.send(f'**<a:RedTick:796628786102927390> You are not cool enough to ban that person.**')
        if ctx.author == user:
            await ctx.send("You cannot ban yourself.")
            return
        if user == discord.Member:
            if ctx.message.author.top_role <= user.top_role:
                await ctx.send(f"**<a:RedTick:796628786102927390> You are not cool enough to ban that person.**")
                return
        elif user.id == self.bot.owner_id:
            await ctx.send(f"**<:smile_yay:849338019306668052> You can ask my Owner to Leave The Server, He will do it himself!**")
            return
        else:
            await guild.ban(user)
            ban_embed = discord.Embed(description=f'**<:verifiedserver:796628753005543444> ``{user}`` was successfully banned!**', color=0x3498DB)
            ban_msg = f"``` You have been banned from {ctx.guild.name} for {reason} by the Moderator - {ctx.author.name}```"
            await ctx.send(embed=ban_embed)
            await user.send(ban_msg)

#unban CMD

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, user: discord.User):
        try:
            guild = ctx.guild
            await guild.unban(user)
            unban_embed = discord.Embed(description=f'**<:verifiedserver:796628753005543444> ``{user.name}`` was unbanned!**', color=0x3498DB)
            unban_msg = f"``` You have been unbanned from {ctx.guild.name} by the Moderator - {ctx.author.name}```"
            await ctx.send(embed=unban_embed)
            await user.send(unban_msg)
        except:
            await ctx.send(f"**<a:RedTick:796628786102927390> There was some issue in unbanning the member. Make sure to check that u gave correct id and Try Again. **")

        """
        async def unban(self, ctx, *, member):
                banned_users = await ctx.guild.bans()
                member_name, member_discriminator = member.split('#')

                for ban_entry in banned_users:
                    user = ban_entry.user

                    if (user.name, user.discriminator) == (member_name, member_discriminator):
        """

#mute CMD

    @commands.command(aliases=['tempmute'])
    async def mute(self, ctx, member: discord.Member=None, time=None, *, reason=None):
        if not member:
            await ctx.send("You must mention a member to mute!")
            
        if member == ctx.guild.owner:
            return await ctx.send(f'**<a:RedTick:796628786102927390> You are not cool enough to mute that person.**')

        if ctx.message.author.top_role <= member.top_role:
            await ctx.send(f"**<a:RedTick:796628786102927390> You are not cool enough to mute that person.**")
            return

        elif not time:
            await ctx.send("You must mention a time!")

        else:
            if not reason:
                reason="No reason given"
            #Now timed mute manipulation

            try:
                seconds = int(time[:-1]) #Gets the numbers from the time argument, start to -1
                duration = time[-1] #Gets the timed maniulation, s, m, h, d
                if duration == "s":
                    seconds = seconds * 1
                elif duration == "m":
                    seconds = seconds * 60
                elif duration == "h":
                    seconds = seconds * 60 * 60
                elif duration == "d":
                    seconds = seconds * 86400
                else:
                    await ctx.send("Invalid duration input")
                    return

            except Exception as e:
                print(e)
                await ctx.send("Invalid time input")
                return

            guild = ctx.guild
            Muted = discord.utils.get(guild.roles, name="Muted")

            if not Muted:
                Muted = await guild.create_role(name="Muted")

                for channel in guild.channels:
                    await channel.set_permissions(Muted, speak=False, send_messages=False, read_message_history=True, read_messages=False)
            
            await member.add_roles(Muted, reason=reason)
            muted_embed = discord.Embed(title="New Punishment!", description=f"🤐 You were muted by {ctx.author.mention} for **{time}** coz of reason: **{reason}** in server **{guild.name}**", color=0xE91E63)
            await ctx.send(f":ok_hand: {member.mention} was successfully muted!")
            try:
                await member.send(embed=muted_embed)
            except HTTPException:
                pass
            await asyncio.sleep(seconds)
            await member.remove_roles(Muted)
            unmute_embed = discord.Embed(title="Mute over!", description=f'Your mute of time: {time} is over now!\n Reason was: `{reason}`\n Make sure not to repeat it again!', color=0xE91E63)
            try:
                await member.send(embed=unmute_embed)
            except HTTPException:
                pass


#unmute CMD           

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def unmute(self, ctx, member: discord.Member):
        role = discord.utils.get(ctx.guild.roles, name= "Muted")
        if role in member.roles:
            await member.remove_roles(role)
            unmute_msg = f"``` You have been un-muted in {ctx.guild.name} by the Moderator - {ctx.author.name}```"
            await ctx.send(f"{member.mention} was unmuted.")
            try:
                await member.send(unmute_msg)
            except HTTPException:
                pass
        else:
            await ctx.send(f"**Is That Person even muted? <:hmm:815854699084644352>**")

#DMuser CMD

    @commands.command(aliases=['pmuser'], hidden=True)
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    async def DMuser(self, ctx, user: discord.User, *, msg):
        try:
            await user.send(f'**{ctx.message.author}** has a message for you, \n > {msg}')
        except:
            await ctx.send(f'<a:RedTick:796628786102927390> The user has his/her DMs turned off.')
            
#purge CMD

    @commands.command(aliases=['purge'], hidden=True)
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=3):
        if amount <= 200:
            await ctx.channel.purge(limit=amount+1)
            await ctx.send(f'**The higher-ups have purged some messages.**', delete_after=10)

        else:
            await ctx.send("Please add a number smaller than 200")

#purge user cmd

    @commands.command(aliases=['clearuser'], hidden=True)
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    async def purgeuser(self, ctx, user: discord.Member,
                        num_messages: typing.Optional[int] = 100,
                        ):

        channel = ctx.message.channel
        if ctx.guild.me.top_role < user.top_role:
            return await ctx.send(f"<a:RedTick:796628786102927390> The member has higher role than me!")
        if ctx.message.author.top_role < user.top_role:
            return await ctx.send(f"**<a:RedTick:796628786102927390> You are not cool enough to delete their messages**")

        def check(msg):
            return msg.author.id == user.id

        await ctx.message.delete()
        await channel.purge(limit=num_messages, check=check, before=None)
        await ctx.send(f'**The higher-ups have purged someone\'s messsages.**', delete_after=10)    

# nuke COMMAND

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def nuke(self, ctx):
        channel = ctx.channel
        positions = ctx.channel.position
        n = await channel.clone()
        await n.edit(position=positions)
        await channel.delete()
        await n.send(" :ok_hand: Successfully Nuked this channel")
        await n.send("https://giphy.com/gifs/animation-explosion-bomb-FnatKdwxRxpVC?utm_source=media-link&utm_medium=landing&utm_campaign=Media%20Links&utm_term=")

# role 

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    @commands.guild_only()
    async def role(self, ctx, member: discord.Member, *, role : discord.Role):
        if ctx.guild.me.top_role < member.top_role:
            return await ctx.send(f"**<a:RedTick:796628786102927390> The member has higher role than me!**")
        if role is None:
            return await ctx.send(f"**<:hmm:815854699084644352> You sure that is a role? Coz I couldn't find it.**")
        if ctx.message.author.top_role.position <= role.position:
            return await ctx.send(f"**<a:RedTick:796628786102927390> That role is higher than or same as your top-most role!**")

        if role not in member.roles:
            await member.add_roles(role)
            await ctx.send(f"{member} was given role `{role.name}`.")
        else:
            await member.remove_roles(role)
            await ctx.send(f"{member} was removed from the role `{role.name}`.")

# slowmode

    @commands.command(aliases=['sm'])
    @commands.guild_only()
    @commands.has_permissions(manage_roles=True)
    async def slowmode(self, ctx, time):
        if time == 'remove':
            await ctx.channel.edit(slowmode_delay=0)
            await ctx.send(f'Slowmode removed.')


        else:

            await ctx.channel.edit(slowmode_delay=time)
            await ctx.send(f'{time}s of slowmode was set on the current channel.')


# channel lock
    @commands.command(hidden=True)
    @commands.guild_only()
    @commands.has_permissions(manage_channels=True)
    async def lock(self, ctx):
        overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
        overwrite.send_messages = False
        await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
        await ctx.send("🔒 Channel locked down. Only staff members may speak. Do not bring the topic to other channels or risk disciplinary actions.")

#channel unlock

    @commands.command(hidden=True)
    @commands.guild_only()
    @commands.has_permissions(manage_channels=True)
    async def unlock(self, ctx):
        overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
        overwrite.send_messages = True
        await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
        await ctx.send("🔒 Channel unlocked. Don't mess or spam in the channel :)")

def setup(Bot):
    Bot.add_cog(Mod(Bot))
    print("Mod cog is Loaded!")
