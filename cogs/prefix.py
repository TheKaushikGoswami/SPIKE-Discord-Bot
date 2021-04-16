import discord
import json
from discord.ext import commands
import sys

class Prefix(commands.Cog, name='Prefix'):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_guild = True)
    async def set_prefix(self, ctx, *, prefix):

        with open("prefixes.json", "r") as f:
            prefixes = json.load(f)


        prefixes[str(ctx.guild.id)] = prefix

        with open(r"prefixes.json", "w") as f:
            json.dump(prefixes, f, indent=4)

        await ctx.send(f"**`{prefix}` is the new prefix for this guild !**")

def setup(bot):
    bot.add_cog(Prefix(bot))
    print("Prefix cog is Working!")