from discord.ext import commands
import os

class Music(commands.Cog, name='Music'):

    def __init__(self,bot):
        self.bot = bot

        