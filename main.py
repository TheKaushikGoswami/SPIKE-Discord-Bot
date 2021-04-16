import discord
from discord.ext import commands
import discord.utils
import json
import asyncio
import random
import sys
import os
import traceback
from pathlib import Path # For paths
import platform
import praw
# import asyncpg



# SETUP

def get_prefix(bot, message):
    if not message.guild:
        return commands.when_mentioned_or("sp!")(bot, message)

    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    if str(message.guild.id) not in prefixes:
        return commands.when_mentioned_or("sp!")(bot,message)

    prefix = prefixes[str(message.guild.id)]
    return commands.when_mentioned_or(prefix)(bot, message)

cwd = Path(__file__).parents[0]
cwd = str(cwd)
print(f"{cwd}\n-----")



intents = discord.Intents.all()
bot = commands.Bot(command_prefix=get_prefix, case_insensitive=True, intents=intents, owner_id=737903565313409095)
bot.remove_command("help")
bot.color = 0xa100f2
bot.guild_id = 773185292211453974
bot.github = "https://github.com/TheKaushikGoswami/SPIKE-PY.git"


# EVENTS

@bot.event
async def on_ready():
    
    await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.listening, name=f".help | Made with ❤️ by KAUSHIK | In {len(bot.guilds)} servers!"))
    
    print("Hello There! I m Ready... :D")

    async def ch_pr():
        await bot.wait_until_ready()

        statuses = [f"sp!help | In {len(bot.guilds)} servers!", "sp!help | TG Network" , "sp!help | KAUSHIK, YUVII, NICKY, PHANTOM & SHREYASH", "sp!help | Made with ❤️ by KAUSHIK", f"{len(set(bot.get_all_members()))} Members in {len(bot.guilds)} Servers!"]

        while not bot.is_closed():

            status = random.choice(statuses)

            await bot.change_presence(status = discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name=status))

            await asyncio.sleep(7)

    bot.loop.create_task(ch_pr())


#ERROR HANDLING

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f"{ctx.message.author.mention} <a:RedTick:796628786102927390> You don't meet all the requirements to use this command.")
    if isinstance(error, commands.CommandOnCooldown):
        msg = " The command is on **Cooldown!** Try again after **{:.2f}s!**".format(
            error.retry_after)
        await ctx.send(f'**{ctx.message.author.mention}, {msg}**')

    if isinstance(error, commands.MissingRequiredArgument) or isinstance(error, commands.BadArgument):
        helper = str(ctx.invoked_subcommand) if ctx.invoked_subcommand else str(
            ctx.command)
        await ctx.send(f'** {ctx.author.mention} The correct way of using that command is:** ')
        await ctx.send_help(helper)
        
# COLORS

bot.colors = {
    "WHITE": 0x26fcff,
    "AQUA": 0x1ABC9C,
    "GREEN": 0x2ECC71,
    "BLUE": 0x3498DB,
    "PURPLE": 0x9B59B6,
    "LUMINOUS_VIVID_PINK": 0xE91E63,
    "GOLD": 0xF1C40F,
    "ORANGE": 0xE67E22,
    "RED": 0xE74C3C,
    "NAVY": 0x34495E,
    "DARK_AQUA": 0x11806A,
    "DARK_GREEN": 0x1F8B4C,
    "DARK_BLUE": 0x206694,
    "DARK_PURPLE": 0x71368A,
    "DARK_VIVID_PINK": 0xAD1457,
    "DARK_GOLD": 0xC27C0E,
    "DARK_ORANGE": 0xA84300,
    "DARK_RED": 0x992D22,
    "DARK_NAVY": 0xe8c02a,
    "Hm": 0xebf54c
}
bot.color_list = [c for c in bot.colors.values()]

# filtered words
filtered_words = ["porn"]

@bot.event
async def on_message(msg):
    for word in filtered_words:
        if word in msg.content:
            await msg.delete()

    await bot.process_commands(msg)

# COGS SETUP

extensions=[
            'cogs.fun',
            'cogs.utility',
            'cogs.mod_cmds',
            'cogs.nqn',
            'cogs.owner',
            'cogs.api_cmd',
         #   'cogs.prefix',
            'cogs.help',
        #    'cogs.giveaway',
          #  'cogs.welcome',
        #    'cogs.channel',
            'cogs.snap',
            'cogs.say'
]
if __name__ == "__main__":
    for extension in extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(e)
            traceback.print_exc()

# asyncpg
"""

async def create_db_pool():
    bot.db = await asyncpg.create_pool(database="SPIKE" ,user="postgres" , password='TheKaushik@1')
    print("Succesfully Connected To Database!")

bot.loop.create_task(create_db_pool())
"""

#SPECIAL CMD

reddit = praw.Reddit(client_id='HjbmApr9tS0P9A',
                     client_secret='ni7CCh_wEVxJv_HwI4VSZcCpjP9zhQ',
                     user_agent='SPIKE by u/TheKaushik01',
                     check_for_async=False)
"""
@bot.command()
@commands.cooldown(1, 15, commands.BucketType.user)
async def mc(ctx):
    memes_submissions = reddit.subreddit('minecraftmemes').hot()
    post_to_pick = random.randint(1, 1000)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)
    e = discord.Embed(color=random.choice(bot.color_list))
    e.set_image(url=f'{submission.url}')
    e.set_footer(text=f'Requested by {ctx.author.name}, Source : r/MinecraftMemes',icon_url=ctx.author.avatar_url)
    await ctx.send(embed=e)
"""

# TOKEN

bot.run("Your-Token-Here")
