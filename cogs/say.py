import discord
from discord.ext import commands
import asyncio
import random

class Say(commands.Cog, name='Say'):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def say(self, ctx, title, *, word):
        em = discord.Embed(title=f'{title}', description=f'{word}', color=random.choice(self.bot.color_list))
        await ctx.send(embed=em)

def setup(bot):
    bot.add_cog(Say(bot))
    print("Say Cog is loaded!")