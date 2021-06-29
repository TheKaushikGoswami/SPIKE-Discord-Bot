import discord
from discord.ext import commands
import asyncio
import random
import datetime

class Say(commands.Cog, name='Say'):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def embed(self, ctx, title, *, word):
        await ctx.channel.purge(limit=1)
        em = discord.Embed(title=f'{title}', description=f'{word}', color=random.choice(self.bot.color_list), timestamp=datetime.datetime.utcnow())
        em.set_footer(text=f"By {ctx.author.name}")
        await ctx.send(embed=em)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def say(self, ctx, *, message):
        await ctx.channel.purge(limit=1)
        await ctx.send(message)

def setup(bot):
    bot.add_cog(Say(bot))
    print("Say Cog is loaded!")