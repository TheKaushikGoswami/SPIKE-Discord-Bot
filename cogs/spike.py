import discord, datetime, time
from discord.ext import commands
import sys
import datetime
import random
import platform
import time
from ago import human
import collections
from discord.ext.commands import bot
import discord.utils

start_time = time.time()

class SPIKE(commands.Cog, name='SPIKE'):

    def __init__(self,bot):
        self.bot = bot
    

#ping advanced
    @commands.command(description='Advanced ping command for the nerds out there.')
    async def ping(self, ctx):
        # nerdy stufss here
        msg = await ctx.send("Pinging bot\'s latency...")
        times = []
        counter=0
        embed = discord.Embed(title="More information:", description="Pinged 3 times and calculated the average.", color = ctx.author.color)


        for _ in range(3):
            counter += 1
            start = time.perf_counter()
            await msg.edit(content=f"Pinging... {counter}/3")
            end = time.perf_counter()
            speed = round((end - start) * 1000)
            times.append(speed)
            embed.add_field(name=f"Ping {counter}:", value=f"{speed}ms", inline=True)

        embed.set_author(name="Pong!", icon_url= ctx.author.avatar_url)
        embed.add_field(name="Bot latency", value=f"{round(self.bot.latency * 1000)}ms", inline=True)
        embed.add_field(name="Average speed", value=f"{round((round(sum(times)) + round(self.bot.latency * 1000))/4)}ms")
        embed.set_thumbnail(url= ctx.guild.icon_url)
        embed.set_footer(text=f"Estimated total time elapsed: {round(sum(times))}ms")
        await msg.edit(content=f":ping_pong: {round((round(sum(times)) + round(self.bot.latency * 1000))/4)}ms", embed=embed)

#invite COMMAND

    @commands.command()
    async def invite(self, ctx):
        await ctx.send(f"**{ctx.author.mention}, Invite Me by Clicking this link** ❯ https://discord.com/api/oauth2/authorize?client_id=773180092015968316&permissions=8&scope=bot")

#support

    @commands.command()
    async def support(self, ctx):
        await ctx.send(f"https://discord.gg/VYDq5AheEU")
        await ctx.send(f"👆 Join The Above Server for all support related to **SPIKE**")

#uptime CMD

    @commands.command(pass_context=True)
    async def uptime(self, ctx):
        current_time = time.time()
        difference = int(round(current_time - start_time))
        text = str(datetime.timedelta(seconds=difference))
        embed = discord.Embed(colour=ctx.message.author.top_role.colour)
        embed.add_field(name="Uptime", value=text)
        embed.set_footer(text="UwU")
        try:
            await ctx.send(embed=embed)
        except discord.HTTPException:
            await ctx.send("Current uptime: " + text)
        

#about CMD

    @commands.Cog.listener()
    async def on_ready(self):
        global startTime #global variable to be used later in cog
        startTime = time.time()# snapshot of time when listener sends on_ready

    @commands.command(description=f"Lemme Introduce Myself To You ;D", aliases=['me', 'botinfo'])
    async def about(self, ctx):
        pythonVersion = platform.python_version()
        dpyVersion = discord.__version__
        uptime = str(datetime.timedelta(seconds=int(round(time.time()-startTime))))
        embed=discord.Embed(title="About SPIKE", description=f"**SPIKE** is a bot that can do most of the things that everything you require for making a better and better Discord Server. The bot is user-friendly too, to make it comfortable for everyone to get familiar with discord bots and stuff.", color=0x5de5c9, timestamp=datetime.datetime.utcnow())
        embed.set_thumbnail(url=f'{ctx.me.avatar_url}')
        embed.add_field(name=f"__General Details__", value=f"**❯ Bot:** SPIKE#4583 (773180092015968316)\n **❯ Created On:** 3rd November 2020, 1:41:38 PM IST\n **❯ Uptime:** ``{uptime}``\n **❯ Developer:** ``_TheKaushikG_#5300`` (<@737903565313409095>)", inline=False)
        embed.add_field(name=f"__Front-end Stats__", value=f"**❯ Servers:** {len(self.bot.guilds)}\n **❯ Channels:** {len(set(self.bot.get_all_channels()))}\n **❯ Users:** {len(set(self.bot.get_all_members()))}", inline=True)
        embed.add_field(name=f"__Back-end Stats__", value=f"**❯ Version:** [v2.0.2](https://github.com/TheKaushikGoswami/SPIKE-Discord-Bot)\n **❯ Python version:** [v{pythonVersion}](https://python.org)\n **❯ discord.py version:** [v{dpyVersion}](https://discordpy.readthedocs.io/en/stable)\n **❯ Modules:** Total 15 modules", inline=False)
        embed.add_field(name="__Check Out:__", value=f'[Invite](https://discord.com/api/oauth2/authorize?client_id=773180092015968316&permissions=8&scope=bot) • [Support](https://discord.gg/VYDq5AheEU) • [Github](https://github.com/TheKaushikGoswami/SPIKE-Discord-Bot) • [Github Me](https://github.com/TheKaushikGoswami)')
        embed.set_image(url=f'https://media.discordapp.net/attachments/821649522672926740/845695162905919518/SPIKE-banner.png?width=1395&height=349')
        embed.set_footer(icon_url=f'{ctx.me.avatar_url}', text=f"SPIKE is made with ❤️")
        await ctx.send(embed=embed)

#setup COMMAND

def setup(bot):
    bot.add_cog(SPIKE(bot))
    print("SPIKE Cog is Loaded!")
