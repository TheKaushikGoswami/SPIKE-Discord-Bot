"""
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
"""

import discord
from discord.ext import commands
from disputils import BotEmbedPaginator
from cogs.utils import Pag
import datetime

color = 0x1ABC9C
nomasti = 'https://pbs.twimg.com/media/EUqVvbQUcAAtL1H.jpg'
ban = 'https://cdn.discordapp.com/attachments/821649522672926740/839494104755732500/ban_and_unban.gif'
slowmode = 'https://cdn.discordapp.com/attachments/821649522672926740/839494107051196426/slowmode.gif'
role = 'https://cdn.discordapp.com/attachments/821649522672926740/839494147332767804/role.gif'
nickname = 'https://cdn.discordapp.com/attachments/821649522672926740/839494615081287700/nick.gif'


class SPIKE(commands.Cog, name='Help'):
    def __init__(self, Bot):
        self.bot = Bot
        self.cmds_per_page = 10

    @commands.command()
    @commands.guild_only()
    async def help(self, ctx, *, entity=None):
        if ctx.channel.id == 757108786497585172:
            return

        if not entity:
            embed1 = discord.Embed(
                color=color, description=f"These are the commands which are executable in the **SPIKE**. For additional info on a command, type `sp!help <command>`. For More Info on Moderation Commands, use `sp!helpmod`.", timestamp=datetime.datetime.utcnow())
            embed1.set_author(name="Help Interface",
                              icon_url=f'{ctx.me.avatar_url}')
            embed1.set_thumbnail(
                url=f"https://media2.giphy.com/media/401pPJe8AtsC55e1y8/source.gif")
            embed1.add_field(
                name="🛡️ Moderation", value=f'`nick` `purge` `purgeuser` `mute` `unmute` `kick` `ban` `dmuser` `nuke` `role` `slowmode` `lock` `unlock` `name_role`', inline=False)
            embed1.add_field(
                name="⚽ Fun & Games", value=f'`8ball` `lovemeter` `rps` `sad/happy/angry` `hello` `lenny` `flip` `f` `calculator` `diceroll` `meme` `joke` `password` `slots` `cheers` `simp` `iq` `roast` `kill`',  inline=False)
            embed1.add_field(
                name="🖼️ Images", value=f'`cat` `dog` `panda` `koala` `pikachu` `clyde` `facepalm` `wink` `headpat` `hug` `snap`', inline=False)
            embed1.add_field(
                name="🛠️ Utility", value=f'`userinfo` `serverinfo` `avatar` `membercount` `roleinfo` `channelstats` `dictionary` `say` `embed` `pings` `timer`',  inline=False)
            embed1.add_field(
                name="💭 Facts & Advices", value=f'`dogfact` `catfact` `pandafact` `numberfact` `yearfact` `advice` `aquote` ',   inline=False)
            embed1.add_field(
                name="🤖 SPIKE", value=f'`about` `ping` `invite` `support` `help` `uptime`', inline=False)
            embed1.add_field(
                name=f"👑 Owner Only", value=f'`reload` `unload` `load` `logout` `stats` `echo`', inline=False)

            embed1.set_footer(text=f"SPIKE is made with ❤️", icon_url=f'{ctx.author.avatar_url}')

            embeds = [embed1]
            paginator = BotEmbedPaginator(ctx, embeds)
            await paginator.run()
        else:
            command = self.bot.get_command(entity)
            if command:
                await self.setup_help_pag(ctx, command, command.name)

            else:
                await ctx.send(f"**{entity}** not found.")

    async def return_filtered_commands(self, walkable, ctx):
        filtered = []
        for c in walkable.walk_commands():
            try:
                if c.hidden:
                    continue
                elif c.parent:
                    continue
                await c.can_run(ctx)
                filtered.append(c)
            except commands.CommandError:
                continue
        return self.return_sorted_commands(filtered)

    def return_sorted_commands(self, commandList):
        return sorted(commandList, key=lambda x: x.name)

    def get_command_signature(self, command: commands.Command, ctx: commands.Context):
        aliases = "| ".join(command.aliases)
        cmd_invoke = f'[{command.name} | {command.aliases}]' if command.aliases else command.name
        full_invoke = command.qualified_name.replace(command.name, "")
        signature = f'sp!{full_invoke}{cmd_invoke} {command.signature}'
        return signature

    async def setup_help_pag(self, ctx, entity=None, title=None):
        entity = entity or self.bot
        title = title or self.bot.description

        pages = []

        if isinstance(entity, commands.Command):
            filtered_commands = (
                list(set(entity.all_commands.values()))
                if hasattr(entity, "all_commands")
                else []
            )
            filtered_commands.insert(0, entity)
        else:
            filtered_commands = await self.return_filtered_commands(entity, ctx)

        for i in range(0, len(filtered_commands), self.cmds_per_page):
            next_commands = filtered_commands[i: i + self.cmds_per_page]
            commands_entry = ""

            for cmd in next_commands:
                desc = cmd.short_doc or cmd.description
                signature = self.get_command_signature(cmd, ctx)
                subcommands = "Has subcommands " if hasattr(
                    cmd, "all_commands") else ""
                commands_entry += (
                    f" ```{signature}\n```\n**Description:** {desc}\n"
                    if isinstance(entity, commands.Command)
                    else f"**{cmd.name}**\n{desc}\n    {subcommands}\n"
                )
            pages.append(commands_entry)
        await Pag(title=title, color=color, entries=pages, length=1).start(ctx)

    @commands.command()
    async def help_default(self, ctx, *, entity=None):
        if not entity:
            await self.setup_help_pag(ctx)
        else:
            cog = self.bot.get_cog(entity)
            if cog:
                await self.setup_help_pag(ctx, cog, f"{cog.qualified_name}'s commands")

            else:
                command = self.bot.get_command(entity)
                if command:
                    await self.setup_help_pag(ctx, command, command.name)

                else:
                    await ctx.send(f"{entity} not found.")

    @commands.command(alaises=['moderationcommands'])
    @commands.guild_only()
    async def helpmod(self, ctx):

        embed1 = discord.Embed(color=color)
        embed1.set_author(name="Mod Commands", icon_url=f'{ctx.me.avatar_url}')
        embed1.add_field(name="Purge", value="**Aliases** : Clear\n"
                         "**Limit** : 200 \n"
                         "**Default value** : 3 \n"
                         "**Permission** : Manage messages \n"
                         "**Usage**\n ```sp!purge 10```\n\n"
                         )
        embed1.add_field(name="PurgeUser", value="**Aliases** : Clearuser\n"

                         "**Permission** : Manage messages\n"
                         "**Usage**\n ```sp!purgeuser @_TheKaushikG_#5300 10```\n\n"
                         )

        embed1.add_field(name="Dmuser", value=f"**Aliases** : Pmuser\n"

                         "**Permission** : Manage messages\n"
                         "**Usage**\n ```sp!dmuser @_TheKaushikG_#5300 why is this a command?```\n\n")
        embed1.set_footer(
            text=f"Tip : All the command names are case insensitive.")

        embed2 = discord.Embed(color=color)
        embed2.add_field(name="Kick", value=f"**Aliases** : None\n"

                         "**Permission** : Kick users\n"
                         "**Usage**\n ```sp!kick <user> <Reason>```\n")
        embed2.add_field(name="Ban", value=f"**Aliases** : None\n"

                         "**Permission** : Ban users\n"
                         "**Usage**\n ```sp!ban <user> <Reason>```\n")
        embed2.add_field(name="Unban", value=f"**Aliases** : None\n"

                         "**Permission** : Administrator\n"
                         "**Usage**\n ```sp!unban 737903565313409095```\n"
                         "**Example :** \n\n", inline=False)
        embed2.set_image(url=f'{ban}')
        embed2.set_footer(
            text=f"Tip : Don't Misuse These Perms or This could result in something bad for U ;D. ")
        embed3 = discord.Embed(color=color)

        embed3.add_field(name="nick", value=f"**Aliases** : None\n"

                         "**Permission** : Change nickname\n"
                         "**Usage**\n ```sp!nick @_TheKaushikG_#5300 Kauchik ```\n"
                         "**Example :** \n\n", inline=False)
        embed3.set_image(url=f'{nickname}')

        embed3.set_footer(
            text=f"Tip : Although the commands are insensitive the role names ain't! Be careful.")
        embed4 = discord.Embed(color=color)
        embed4.add_field(name='role', value=f"**Aliases** : None\n"
                                            f'**What for** : To add or remvoe roles to the mentioned user.\n'
                         "**Permission** : Manage roles\n"
                         "**Usage**\n ```sp!role @_TheKaushikG_ Daddy ```\n"
                         "**Example :** \n\n", inline=False)
        embed4.set_image(url=f'{role}')
        embed4.set_footer(
            text='Tip : If used on the user who already has the role, the Bot will remove the role.')
        embed5 = discord.Embed(color=color)
        embed5.add_field(name='Channelstats', value=f"**Aliases** : cstats\n"
                         "**Usage**\n ```sp!channelstats ```\n", inline=False)

        embed5.add_field(name='Slowmode', value=f"**Aliases** : sm\n"
                         "**Permission** : Manage channel"

                                                "**Usage**\n ```sp!slowmode <time> ```\n\n"
                                                "**Example **: ```")
        embed5.set_footer(
            text='Tip : "sp!Slowmode remove" will remove the slowmode. ')
        embed5.set_image(url=f'{slowmode}')
        embed7 = discord.Embed(color=color)
        embed7.add_field(
            name='Lock / Unlock', value=f'**Aliases : **None\n **Permission :** Administrator\n **Usage :** ```sp!lock / sp!unlock```', inline=False)
        embed7.add_field(name='Roleinfo', value=f"**Aliases : **  rinfo\n"

                                                '**Usage**\n ```sp!roleinfo Humans ```\n', inline=False)
        embed7.set_footer(
            text=f'Never ever ask for roles anywhere, The mods don\'t like it')

        embeds = [embed1, embed2, embed3, embed4, embed5, embed7]
        paginator = BotEmbedPaginator(ctx, embeds)
        await paginator.run()

    @commands.command()
    async def embedtest(self, ctx):
        embed1 = discord.Embed(title=f'Page1')
        embed1.add_field(name="This is a page", value="Yep itsure is")
        embed2 = discord.Embed(title=f'Page3')
        embed2.add_field(name="This is a page", value="Yep itsure is")
        embed3 = discord.Embed(title=f'Page3')
        embed3.add_field(name="This is a page", value="Yep itsure is")
        embeds = [embed1, embed2, embed3]
        paginator = BotEmbedPaginator(ctx, embeds)
        await paginator.run()


def setup(Bot):
    Bot.add_cog(SPIKE(Bot))
    print("Help cog is working.")
