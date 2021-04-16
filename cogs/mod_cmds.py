import discord
from discord.ext import commands
from discord import User
import datetime
import typing
from datetime import datetime

class Mod(commands.Cog, name='Mod'):

    def __init__(self,bot):
        self.bot = bot

#nick CMD

    @commands.command()
    @commands.has_permissions(manage_nicknames=True)
    async def nick(self, ctx, member: discord.Member, *, nick):
        if ctx.guild.me.top_role < member.top_role:
            return await ctx.send("**<a:RedTick:796628786102927390> This Member has A Greater Role Than Me...**")
        if ctx.message.author.top_role < member.top_role:
            return await ctx.send("**<a:RedTick:796628786102927390> You don't have perms to use that cmd on that person....**")
        else:
            await member.edit(nick=nick)
            await ctx.send(f'```{member} nickname was changed to {nick} by {ctx.message.author}```')

#kick CMD

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, user : discord.Member, *, reason = None):
        """Kicks a user from the server."""
        if ctx.author == user:
            await ctx.send("You cannot kick yourself.")
        else:
            await user.kick()
            kick_msg = f"``` You have been kicked from {ctx.guild.name} for {reason} by the Moderator - {ctx.author.name}```"
            kick_embed = discord.Embed(title=f'User {user.name} has been kicked.', color=0x206694)
            kick_embed.add_field(name="Goodbye!", value=":boot:")
            kick_embed.set_thumbnail(url=user.avatar_url)
            await ctx.send(embed=kick_embed)

#ban CMD

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, user : discord.Member, *, reason =None):
        if ctx.author == user:
            await ctx.send("You cannot ban yourself.")
        else:
            await user.ban()
            ban_embed = discord.Embed(title=f'{user.name} has been banned.', color=0xE74C3C)
            ban_embed.add_field(name="Goodbye!", value=":hammer:")
            ban_embed.set_thumbnail(url=user.avatar_url)
            ban_msg = f"``` You have been banned from {ctx.guild.name} for {reason} by the Moderator - {ctx.author.name}```"
            await ctx.send(embed=ban_embed)
            await user.send(ban_msg)

#id BAN CMD

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def idban(self, ctx, id : int, *, reason = None):
        guild = ctx.guild
        await guild.ban(discord.Object(id))
        idban_embed = discord.Embed(title=f' {self.bot.get_user(id).name} has been banned.', color=0xE74C3C)
        idban_embed.add_field(name="Goodbye!", value=":hammer:")
        idban_embed.set_thumbnail(url = self.bot.get_user(id).avatar_url)
        idban_msg = f"``` You have been banned from {ctx.guild.name} for {reason} by the Moderator - {ctx.author.name}```"
        await ctx.channel.send(embed=idban_embed)
        await self.bot.get_user(id).send(idban_msg)

#unban CMD

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, id: int):
        guild = ctx.guild
        await guild.unban(discord.Object(id))
        unban_embed = discord.Embed(title=f'{self.bot.get_user(id).name} has been unbanned.', color=0x00ff00)
        unban_embed.add_field(name="**Nice! Enjoy... :D**", value=":smile:")
        unban_embed.set_thumbnail(url = self.bot.get_user(id).avatar_url)
        unban_msg = f"``` You have been unbanned from {ctx.guild.name} by the Moderator - {ctx.author.name}```"
        await ctx.channel.send(embed=unban_embed)
        await self.bot.get_user(id).send(unban_msg)

        """
        async def unban(self, ctx, *, member):
                banned_users = await ctx.guild.bans()
                member_name, member_discriminator = member.split('#')

                for ban_entry in banned_users:
                    user = ban_entry.user

                    if (user.name, user.discriminator) == (member_name, member_discriminator):
        """

#mute CMD

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def mute(self ,ctx, member: discord.Member, time, *, reason=None):
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        time_convert = {"s":1, "m":60, "h":3600,"d":86400}
        tempmute= int(time[0]) * time_convert[time[-1]]
        guild = ctx.guild
        if role not in guild.roles:
            perms = discord.Permissions(send_messages=False, speak=False)
            await guild.create_role(name="Muted", permissions=perms)
            await member.add_roles(role)
            mute_msg = f"``` You have been muted in {ctx.guild.name} for reason {reason} by the Moderator - {ctx.author.name}```"
            await member.send(mute_msg)
            await ctx.send(f":ok_hand: {member.mention} was muted successfully for reason **{reason}**.")
        else:
            await member.add_roles(role)
            await ctx.send(f":ok_hand: {member.mention} was muted successfully for reason **{reason}**.")
            await member.send(mute_msg)

#unmute CMD           

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def unmute(self, ctx, member: discord.Member):
        role = discord.utils.get(ctx.guild.roles, name= "Muted")
        await member.remove_roles(role)
        unmute_msg = f"``` You have been un-muted in {ctx.guild.name} by the Moderator - {ctx.author.name}```"
        await ctx.send(f"{member.mention} was unmuted.")
        await member.send(unmute_msg)

#dm CMD

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def dm(self, ctx, id: int, *, msg):
        dm_user = self.bot.get_user(id)
        try:
            await dm_user.send(msg)
            await ctx.send("** The User Has Been DMed...**")

        except:
            await ctx.send("** User Has His DMs OFF... D:**")

#purge CMD

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def purge(self,ctx, amount: int):
        await ctx.channel.purge(limit=amount+1)
        await ctx.send('The messages have been cleared Successfully! :smirk: ')
        await ctx.channel.purge(limit=1)

#name_role CMD

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def name_role(self ,ctx, member: discord.Member):
        namerole = discord.utils.get(ctx.guild.roles, name=f'{member.name}')
        guild = ctx.guild
        if namerole not in guild.roles:
            await guild.create_role(name=f"{member.name}")
            await member.add_roles(namerole)
            await ctx.send(f"{member.name} was given the name role.")
        else:
            await member.add_roles(namerole)
            await ctx.send(f"**```{member.name} was given the name role.```**")    

# nuke COMMAND

    @commands.command()
    @commands.has_permissions(administrator=True)
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
    async def role(self, ctx, member: discord.Member, *, role_name):
        if ctx.guild.me.top_role < member.top_role:
            return await ctx.send("Admin :(")
        if ctx.message.author.top_role < member.top_role:
            return await ctx.send("You  have lower roles.")
        role = discord.utils.get(ctx.guild.roles, name=f"{role_name}")

        if role not in member.roles:
            await member.add_roles(role)
            await ctx.send(f"{member} was given role ``{role_name}``.")
        else:
            await member.remove_roles(role)
            await ctx.send(f"{member} was removed from the role ``{role_name}``.")

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
    @commands.has_permissions(administrator=True)
    async def lock(self, ctx):
        overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
        overwrite.send_messages = False
        await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
        await ctx.send("🔒 Channel locked down. Only staff members may speak. Do not bring the topic to other channels or risk disciplinary actions.")

#channel unlock

    @commands.command(hidden=True)
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def unlock(self, ctx):
        overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
        overwrite.send_messages = True
        await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
        await ctx.send("🔒 Channel unlocked. Don't mess or spam in the channel :)")

def setup(Bot):
    Bot.add_cog(Mod(Bot))
    print("Mod cog is Loaded!")
