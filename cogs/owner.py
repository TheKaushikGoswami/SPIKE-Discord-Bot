import discord
from discord.ext import commands
import platform
import sys
import random
import traceback
import os
import asyncio
import aiohttp
import importlib
import json
import utils

guild = 773185292211453974
OWNERID = 737903565313409095

class Owner(commands.Cog, name = 'Owner'):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def stats(self, ctx):
    
        pythonVersion = platform.python_version()
        dpyVersion = discord.__version__
        serverCount = len(self.bot.guilds)
        memberCount = len(set(self.bot.get_all_members()))

        embed = discord.Embed(title=f'{self.bot.user.name} Stats', description='\uFEFF', colour=ctx.author.colour, timestamp=ctx.message.created_at)
        embed.set_thumbnail(url=f"{self.bot.user.avatar_url}")
        embed.add_field(name='Python Version:', value=pythonVersion)
        embed.add_field(name='Discord.Py Version', value=dpyVersion)
        embed.add_field(name='Total Guilds:', value=serverCount)
        embed.add_field(name='Total Users:', value=memberCount)
        embed.add_field(name='Bot Developers:', value="<@737903565313409095>")

        embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)

        await ctx.send(embed=embed)

    #spam CMD.

    @commands.command()
    @commands.is_owner()
    async def mention(self,ctx, *, member : discord.User):
        await ctx.send(f'{member.mention}')
        await ctx.send(f'{member.mention}')
        await ctx.send(f'{member.mention}')
        await ctx.send(f'{member.mention}')
        await ctx.send(f'{member.mention}')

    @commands.command(aliases=['close', 'stopbot'])
    @commands.is_owner()
    async def logout(self, ctx):
        await ctx.send(f"Hey {ctx.author.mention}, I am now logging out :wave:")
        await self.bot.close()

    @logout.error
    async def logout_error(self, ctx, error):
        """
        Whenever the logout command has an error this will be tripped.
        """
        if isinstance(error, commands.CheckFailure):
            await ctx.send("Hey! You lack permission to use this command as you do not own the bot.")
        else:
            raise error

    @commands.command()
    @commands.is_owner()
    async def echo(self, ctx, *, message=None):
        """
        A simple command that repeats the users input back to them.
        """
        message = message or "Please provide the message to be repeated."
        await ctx.message.delete()
        await ctx.send(message)

    @commands.command()
    @commands.is_owner()
    @commands.has_permissions(administrator=True)
    async def server(self, ctx):
        color = 0xa100f2
        embed = discord.Embed(color=color, title=f'ㅤㅤㅤㅤㅤㅤㅤㅤㅤ         SPIKE')
        embed.set_thumbnail(url=f"{self.bot.user.avatar_url}")
        embed.add_field(name='<a:Star:815872623581069343> WELCOME! <a:Star:815872623581069343>', value=f'<a:whitearrow:815872074689019914> Welcome to SPIKE. This may be your first time at the server, I and the staff team thanks you for joining our community server.\n\n <a:whitearrow:815872074689019914> Please read the following sets of information before heading off to the chat section. Also be sure to suggest us about the things we can improve on, only then we can grow together :)')
        embed.add_field(name='<a:Star:815872623581069343> Introduction! <a:Star:815872623581069343>',
                        value=f'<a:whitearrow:815872074689019914> SPIKE is a chat + dev-server based on the combination of various developers which are free to share their ideas here. \n\n <a:whitearrow:815872074689019914> The server allows almost everthing which is within the restrictions of [Discord TOS](https://discord.com/terms). \n\n <a:whitearrow:815872074689019914> The server doesnot have any fixed location, it is a global server which accepts all types of devs. \n\n <a:whitearrow:815872074689019914> SPIKE is made for those who are in love with geeky things and developing and all (While it is also the OFFICIAL SUPPORT OF THE BOT - SPIKE), to interact with each other and also to promote the fantasy genre.', inline=False)
        embed.add_field(name=f'What we offer <a:Duddhu_Op:815854721361248257>', value=f'Share codes & get help & support if you have any errors in your codes! \n' 
                        f'**We are here to help you get your bot online and working!**')
        embed.add_field(name='Aspects!', value=f'➤ Custom bot, The SPIKE\n'
                        f'<a:whitearrow:815872074689019914> Contribution from verified developers. \n'
                        f'<a:whitearrow:815872074689019914> Different code channels respectively for different languages.\n'
                        f'<a:whitearrow:815872074689019914> Custom roles, commands, and more for members with enough contribution points.\n'
                        f'<a:whitearrow:815872074689019914> Helpful community\n'
                        f'<a:whitearrow:815872074689019914> Good staff members\n'
                        f'<a:whitearrow:815872074689019914> Organized server \n'
                        f'<a:whitearrow:815872074689019914> Alot of chill talks \n', inline=False)
        embed.add_field(name=f'**PERMANENT INVITE LINK** <a:Duddhu_Op:815854721361248257> ', value=f'https://discord.gg/HKSzU86Tx8')
        await ctx.send(embed=embed)

    @commands.command()
    @commands.is_owner()
    @commands.has_permissions(administrator=True)
    async def rules(self, ctx):
        color = 0xa100f2
        embed = discord.Embed(color=(color))

        embed.add_field(name='<a:Star:815872623581069343> Rules! <a:Star:815872623581069343>', value='**1.** Do not be racist, homophobic, or sexist, it can be overlooked if the other party is fine with it.\n\n'
                        '**2.** You are allowed to curse on someone as long as they do not mind. There are no barred curse words. If there are complaints on one\'s behavior then it may result in certain actions taken from the moderators\n\n'
                        '**3.** You should not offend or antagonize other parties. You never know who the other party may be.\n\n'
                        '**4.** Spamming of texts, emojis, images, etc is strictly prohibited, if found out it may result in a permanent ban from the server.\n\n'
                        '**5.** The server does allow anything under the [Discord TOS](https://discord.com/terms) but it doesn\'t means that we won\'t take actions if the situation is necessary.\n\n', inline=False)
        embed.add_field(name='‎‎‎‏‏‎ ‎', value='**6.** Posts related to the information of another party, private messages, or pictures without their permission will be removed. This is a rigorous  policy, may result in a permanent ban.\n\n'
                        '**7.** Moderators have final judgment on everything, if they ask you to stop doing something then stop. Do not complain if you have been kicked or banned from the server.\n\n'
                        '**8.** You are free to debate about anything, just don\'t force your beliefs on others.\n\n'
                        '**9.** There shouldn\'t be any bullying or bad behavior to new members.\n\n'
                        '**10.** There should not be any sharing of graphical or image posts related to violence, gore, and things that are against Discord TOS \n\n'
                        '**11.** All NSFW content under TOS  are allowed, as long as they are NOT in Non-NSFW channels. This includes gifs, profile pictures, status,etc.\n\n'
                        '**12.** Self-advertising on main channels won\'t be tolerated, asking for roles, permissions, custom commands will result in warns from the moderators.', inline=False)
        emojy = '<:hmm~1:815854699084644352>'
        embed.set_footer(text=f'Give me a hmm if you read through everything.')
        msg = await ctx.send(embed=embed)
        await msg.add_reaction(f"{emojy}")

    # Load command to manage our "Cogs" or extensions
    @commands.command()
    @commands.is_owner()
    async def load(self, ctx, extension):
        # Check if the user running the command is actually the owner of the bot 
        if ctx.author.id == OWNERID:
            self.bot.load_extension(f'cogs.{extension}')
            await ctx.send(f"**Enabled the Cog! `{extension}`**")
        else:
            await ctx.send(f"You are not cool enough to use this command")

    # Unload command to manage our "Cogs" or extensions
    @commands.command()
    @commands.is_owner()
    async def unload(self, ctx, extension):
        # Check if the user running the command is actually the owner of the bot 
        if ctx.author.id == OWNERID:
            self.bot.unload_extension(f'cogs.{extension}')
            await ctx.send(f"**Disabled the Cog! `{extension}`**")
        else:
            await ctx.send(f"You are not cool enough to use this command")

    # Reload command to manage our "Cogs" or extensions
    @commands.command(name = "reload")
    @commands.is_owner()
    async def reload_(self, ctx, extension):
        # Check if the user running the command is actually the owner of the bot 
        if ctx.author.id == OWNERID:
            self.bot.reload_extension(f'cogs.{extension}')
            await ctx.send(f"**Reloaded the Cog! `{extension}`**") 
        else:
            await ctx.send(f"You are not cool enough to use this command")


def setup(bot):
    bot.add_cog(Owner(bot))
    print("Owner cog is Working!")
