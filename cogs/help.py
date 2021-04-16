from disputils import BotEmbedPaginator
import discord
from discord.ext import commands
import random

class Help(commands.Cog, name = 'Help'):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['help'])
    async def _help(self, ctx):
        first_embed = discord.Embed(title="MODERATION COMMANDS", colour=random.choice(self.bot.color_list))
        first_embed.set_thumbnail(url=f"https://media2.giphy.com/media/401pPJe8AtsC55e1y8/source.gif")
        first_embed.add_field(name=f"<:Nice:819852047696134195> Nick (`sp!nick`)", value= f"```Changes nick of the member for this server!```")
        first_embed.add_field(name=f"<:deletthis:819852261965692929> Purge (`sp!purge`)", value=f"```Deletes the msgs from the channel```")
        first_embed.add_field(name=f"<:muted:819860542147395614> Mute (`sp!mute`)", value=f"```Mutes a member for specific time```")
        first_embed.add_field(name=f"<:muted:819860542147395614> Unmute (`sp!unmute`)", value = f"```Unmutes a Muted Member```")
        first_embed.add_field(name=f"<a:kick:820146512679796767> Kick(`sp!kick`)", value=f"```Kicks a member from the server```")
        first_embed.add_field(name=f"<a:ban:820147068429533235> Ban (`sp!ban`)", value=f"```Bans the mentioned member from the server```")
        first_embed.add_field(name=f"<:BAN_id:820147402182492190> IDBan (`sp!idban`)", value=f"```Bans a member using their id instead of Mentioning Them!```")
        first_embed.add_field(name=f"<a:banKitty:820147713164967966> Unban (`sp!unban`)", value=f"```Unbans a Banned member from the server```")
        first_embed.add_field(name=f"<:DM:820147891762102313> DM (`sp!dm`)", value=f"```DMs a User using the bot```")
        first_embed.add_field(name=f"<a:nuke:820148500653670410> Nuke (`sp!nuke`)", value=f"```Nukes the channel and creates a new channel with same perms```")
        first_embed.add_field(name=f"Role (`sp!role`)", value=f"```Gives a specific role to a user by the name of the role```")
        first_embed.add_field(name=f"Slowmode (`sp!sm`)", value=f"```Adds a specific amount of time as slowmode delay for sending messages in the channel```")
        first_embed.add_field(name=f"Lock (`sp!lock`)", value=f"```Locks the channel for normal members, Higher Council can send messages```")
        first_embed.add_field(name=f"Unlock (`sp!unlock`)", value=f"```Unlocks the locked channel for everyone to post their messages```")
        first_embed.add_field(name=f"Name Role (`sp!name_role`)", value=f"```Special CMD to give personal roles to Friends of U in ur server ;D```")
        first_embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)

        second_embed = discord.Embed(title="API COMMANDS", colour=random.choice(self.bot.color_list))
        second_embed.set_thumbnail(url=f"https://media2.giphy.com/media/401pPJe8AtsC55e1y8/source.gif")
        second_embed.add_field(name=f"Api Help (`sp!help_api`)", value= f"```Get a small note of what each cmd in API do```")
        second_embed.add_field(name=f"Cat (`sp!cat`)", value=f"```A Randomly Generated Picture of Kitty```")
        second_embed.add_field(name=f"Cat fact (`sp!catfact`)", value=f"```A Kitty Cat fact about them :)```")
        second_embed.add_field(name=f"Dog (`sp!dogfact`)", value=f"```A Random Picture of Human's Bestie```")
        second_embed.add_field(name=f"Dog fact (`sp!dogfact`)", value=f"```A Woofy Fact about Woofers ;)```")
        second_embed.add_field(name=f"Panda (`sp!panda`)", value=f"```A pic of the Cutie pie animal```")
        second_embed.add_field(name=f"Panda fact (`sp!pandafact`)", value=f"```A Cutie fact of the cutest animal UwU```")
        second_embed.add_field(name=f"Koala (`sp!koala`)", value=f"```A small-lazy, cute animal... Looks Cuteee 0w0```")
        second_embed.add_field(name=f"Pikachu (`sp!pikachu`)", value=f"```A random pic of the Pika-Pika...```")
        second_embed.add_field(name=f"Year fact (`sp!yearfact`)", value=f"```A factie about a Random Year from the depths of History```")
        second_embed.add_field(name=f"Clyde (`sp!clyde`)", value=f"```Make the Clyde Bot say things on behalf of You... xD```")
        second_embed.add_field(name=f"Number fact (`sp!numberfact`)", value=f"```A additional fact derived from the Multiplication of Mathematics...```")
        second_embed.add_field(name=f"Advice (`sp!advice`)", value=f"```The best advices to make your Life happier and better :D```")
        second_embed.add_field(name=f"A Quote (`sp!aquote`)", value=f"```Some best anime quotes for u ;D```")
        second_embed.add_field(name=f"Head Pat (`sp!headpat`)", value=f"```Give a cute headpat to someone :)```")
        second_embed.add_field(name=f"Wink (`sp!wink`)", value=f"```Wink at your bae... UwU```")
        second_embed.add_field(name=f"Hug (`sp!hug`)", value=f"```Give your friends cute HUGGGGGGGGsss....```")
        second_embed.add_field(name=f"Face Palm (`sp!facepalm`)", value=f"```A Palm to the Face... :/```")
        second_embed.add_field(name=f"Define (`sp!define`)", value=f"```Get a dictionary in the bot itself...```")
        second_embed.add_field(name=f"Meme (`sp!meme`)", value=f"```Randomly Generated Memes from best subreddits for u ;D```")
        second_embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)

        third_embed = discord.Embed(title="FUN COMMANDS", colour=random.choice(self.bot.color_list))
        third_embed.set_thumbnail(url=f"https://media2.giphy.com/media/401pPJe8AtsC55e1y8/source.gif")
        third_embed.add_field(name=f"8 ball (`sp!8ball`)", value=f"```Get answers to all of your questions on Discord only```")
        third_embed.add_field(name=f"Love meter (`sp!lovemeter`)", value=f"```Check the Lovemeter between You and Your Partner ;)```")
        third_embed.add_field(name=f"Hello (`sp!hello`)", value=f"```Get Greetings from over 60 languages randomly...```")
        third_embed.add_field(name=f"Lenny (`sp!lenny`)", value=f"```Send a random LENNY Face```")
        third_embed.add_field(name=f"Flip (`sp!flip`)", value=f"```Flip a Coin for your bet```")
        third_embed.add_field(name=f"Happy (`sp!happy`)", value=f"```If you are happy, send sp!happy```")
        third_embed.add_field(name=f"Sad (`sp!sad`)", value=f"```Don\'t be sad :)```")
        third_embed.add_field(name=f"Angry (`sp!angry`)", value=f"```Someone is angry (><)```")
        third_embed.add_field(name=f"F Press (`sp!f`)", value=f"```Send sp!f to pay respects T-T```")
        third_embed.add_field(name=f"Calculator (`sp!calc`)", value=f"```Calculates BODMAS Maths for u :)```")
        third_embed.add_field(name=f"Dice Roll (`sp!roll`)", value=f"```Roles the DICE for u```")
        third_embed.add_field(name=f"Rock-Paper-Scissors (`sp!rps`)", value=f"```Play Rock, Paper, Scissors with me```")
        third_embed.add_field(name=f"Snap (`sp!snap`)", value=f"```Generate fake messages from a user xD```")
        third_embed.add_field(name=f"Say (`sp!say`)", value=f"```Make the bot send your words in a beautiful embed```")
        third_embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
        
        fourth_embed = discord.Embed(title=f"UTILITY COMMANDS", colour=random.choice(self.bot.color_list))
        fourth_embed.set_thumbnail(url=f"https://media2.giphy.com/media/401pPJe8AtsC55e1y8/source.gif")
        fourth_embed.add_field(name=f"Suggest (`sp!suggest`)", value=f"```Post Your suggestions in suggestion-channel by bot```")
        fourth_embed.add_field(name=f"User info (`sp!ui`)", value=f"```Check information of a user```")
        fourth_embed.add_field(name=f"Avatar (`sp!av`)", value=f"```Get the avatar of a user in WEBP/PNG/JPEG or GIF```")
        fourth_embed.add_field(name=f"Member Count (`sp!membercount`)", value=f"```Count the total number of users on the server```")
        fourth_embed.add_field(name=f"Server Info (`sp!serverinfo`)", value=f"```Get the information about server using this command```")
        fourth_embed.add_field(name=f"Role info (`sp!roleinfo`)", value=f"```Get the information about a specific role without mentioning them```")
        fourth_embed.add_field(name=f"Channel Stats (`sp!cstats`)", value=f"```Gives you information about the channel where the command is used```")
        fourth_embed.add_field(name=f"Ping (`sp!ping`)", value=f"```Pings the bot's latency and shows the connection bond of bot and Discord```")

        embeds = [first_embed, second_embed, third_embed, fourth_embed]

        paginator = BotEmbedPaginator(ctx, embeds)
        await paginator.run()

def setup(bot):
    bot.add_cog(Help(bot))
    print("Help cog is Working!")