import discord
from discord.ext import commands, tasks
from discord.ext.commands import clean_content
from discord.ext.tasks import loop
import traceback
import collections
import datetime
from random import choice, randint
from disputils import BotEmbedPaginator, BotMultipleChoice
import time
from ago import human
import pymongo
from pymongo import MongoClient
import random
from random import choice, randint
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from datetime import datetime
import os
import sys
import asyncio
from aiohttp import request



class Fun(commands.Cog, name='Fun'):

    def __init__(self, bot):
        self.bot = bot

# 8ball

    @commands.command(aliases=['8ball'])
    async def _8ball(self, ctx, *, question):
        responses = ['It is certain.',
                     'It is decidedly so.',
                     'Without a doubt.',
                     'Yes – definitely.',
                     'You may rely on it.',
                     'As I see it, yes.',
                     'Most likely.',
                     'Outlook good.',
                     'Yes.',
                     'Signs point to yes.',
                     'Reply hazy, try again.',
                     'Ask again later.',
                     'Better not tell you now.',
                     'Cannot predict now.',
                     'Concentrate and ask again.',
                     "Don't count on it.",
                     'My reply is no.',
                     'My sources say no.',
                     'Outlook not so good.',
                     'Very doubtful.']
        e = discord.Embed(title=f"MAGIC 8-BALL", color=random.choice(self.bot.color_list))
        e.set_thumbnail(url=f'https://media.tenor.com/images/47ceded02690a48da88d02bb7c1f5f46/tenor.gif')
        e.add_field(name=f"🔮Question by {ctx.author}: `{question}`", value=f"**My Magic Foretells me: `{random.choice(responses)}`**",)
        await ctx.send(embed=e)

    @_8ball.error
    async def _8ball_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please ask a Question!')
          
# lovemeter

    @commands.command(description='Oh boy!, a meter that calculates love between two parties.')
    @commands.guild_only()
    @commands.cooldown(1, 15, commands.BucketType.user)
    # uwu sempai do you lowe mew??
    async def lovemeter(self, ctx, name1: clean_content, name2: clean_content):
        # clean_content is a handy thing you may need it :)
        percentage = random.randint(0, 100)

        if 0 <= percentage <= 10:
            result = ['Friendzone',
                      'You sure it was love-meter not friend-meter ',
                      'Dude that is insultingly low.]',
                      'Ahh the classic ``one sided love``',
                      'Just friends?',
                      'Is my meter off today? Can not pick any numbers']

        elif 10 <= percentage <= 30:
            result = ['Huh, just started dating?',
                      'I guess friendzone never ends',
                      'Best-friend zone?',
                      'My meter picked something up']

        elif 30 <= percentage <= 50:
            result = ['Still one sided, next time bud',
                      'There is still alot room for love',
                      'I mean it is a good start',
                      'There is potential']

        elif 50 <= percentage <= 70:
            result = ['I sense love here',
                      'Oh... love birds?',
                      'Love is in the air',
                      'My meter picked something big',
                      'There is still a long road ahead, stay strong :D',
                      'I mean acceptable']

        elif 70 <= percentage <= 90:
            result = ['Just got wed?',
                      'Very good relationship',
                      'I do not talk much with love birds',
                      'My meter says it is looking good ',
                      'Just steps below the perfect match']

        elif 90 <= percentage <= 100:
            result = ['Yoo dude that iss real love',
                      'Romeo and Juliet?',
                      'My meter nearly exploded',
                      'Adam and Eve?',
                      'Match made in heavens']

        if percentage <= 33:
            shipColor = 0x000000
        elif 33 < percentage < 66:
            shipColor = 0xe3ff00
        else:
            shipColor = 0xee66ee

            # ik ik my gif taste is the best no need to appriciate me
        if percentage <= 10:
            gif = "https://media.tenor.com/images/8eb3ea6f8b8e05115a37df84ba03144a/tenor.gif"
        if 10 < percentage <= 30:
            gif = "https://media.tenor.com/images/d9f4ebad1365272d2605a1a5151d501a/tenor.gif"
        if 30 < percentage <= 50:
            gif = "https://media.tenor.com/images/12414d69b8a99bd6dc19275363e17554/tenor.gif"
        if 50 < percentage <= 70:
            gif = "https://64.media.tumblr.com/09efd576d1e31d6dbf2a66eaa07ef6af/tumblr_n52l5bmodz1tt23n5o1_500.gif"
        if 70 < percentage <= 100:
            gif = "https://media.tenor.com/images/d85ef0ba33daf46de0838eba3efe8d08/tenor.gif"

        final_result = random.choice(result)

        embed = discord.Embed(color=shipColor,
                              title=f"Love meter of {name1} and {name2}")
        embed.set_thumbnail(url=f'{gif}')
        embed.add_field(name="Results:", value=f'{percentage}% ', inline=True)

        embed.add_field(name="Personal opinion :",
                        value=f'{final_result}', inline=False)

        embed.set_author(name="SPIKE LOVE-METER")
        embed.set_footer(
            text=f'Requested by {ctx.author}', icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

# hello

    @commands.command(aliases=['Hi', 'Namaste'], description=f'Get greetings from over 60 languages.')
    @commands.guild_only()
    async def hello(self,ctx):
        '''Nothing special just some greetings'''
        greetings = ['Hello', 'Hiya', 'nĭ hăo', 'Namaste', 'Konichiwa', 'Zdravstvuyte', 'Bonjour', 'Guten tag',
                     'Anyoung haseyo', 'Asalaam alaikum', 'Goddag', 'Selamat siang','hola', 'marhabaan  ', 'hyālō',
                     'Sata srī akāla', 'Nggoleki', 'Vandanalu', '   Xin chào', 'Namaskār', 'Vaṇakkam', 'Salām', 'Merhaba', 'Ciao'
                     , 'Sà-wàt-dii', 'Kaixo', 'Cześć’', 'Namaskāra', 'Prannam', 'Kamusta', 'Hallo', 'Yasou', 'Hej', 'oi', 'Wazza', 'kem cho',
                     'Hai', 'doki-doki', 'meow meow ', 'Lí-hó', 'Vitaju' , 'Bok', 'Hej', 'Moi', 'Sveika /Sveiks ', 'God dag',
                     'Moïen ', 'Vitayu ', 'Aloha ', 'Wassup', 'Howdy!']
        reply = random.choice(greetings)
        await ctx.send(f'{reply}, {ctx.message.author.mention} How is it going for you? No need to ask me, but I am mostly good.')

#lenny

    @commands.command(aliases=['lennyface'], description='Send a random lenny face.')
    @commands.guild_only()
    # sends a random lenny from my collection 

    async def lenny( self, ctx):
        lennys= ['( ͡° ͜ʖ ͡°)', 'ಠ_ಠ', '( ͡ʘ ͜ʖ ͡ʘ)', '(▀̿Ĺ̯▀̿ ̿)', '( ͡°( ͡° ͜ʖ( ͡° ͜ʖ ͡°)ʖ ͡°) ͡°)', '( ͡ᵔ ͜ʖ ͡ᵔ )',
                 '(╯ ͠° ͟ʖ ͡°)╯┻━┻', 'ᕙ(▀̿̿Ĺ̯̿̿▀̿ ̿) ᕗ', '(✿╹◡╹)', 'щ（ﾟДﾟщ） < "Dear god why‽ )', '(人◕ω◕)', '(*бωб)', 'ヽ(͡◕ ͜ʖ ͡◕)ﾉ',
                 '(⌐▀͡ ̯ʖ▀)︻̷┻̿═━一-', 'ᕕ(╯°□°)ᕗ' ]
        await ctx.send(random.choice(lennys))
        await ctx.message.delete()

#flip

    @commands.command(aliases=['coin'], description='Flip a coin.')
    @commands.guild_only()

    async def flip(self, ctx):
        # tails
        value=[f"<:heads:820703848489680907>", f"<:tails:820703918652784640>"]

        fliping = await ctx.send(f"https://i.pinimg.com/originals/52/91/f5/5291f56897d748b1ca0a10c90023588d.gif")

        await asyncio.sleep(10)

        flip = random.choice(value)

        if flip == f"<:tails:820703918652784640>":

            await ctx.send(f"**The coin flipped and gave u a `Tails`**")
            await fliping.edit(content=f'{flip}')

        else:
            await ctx.send(f"**The coin flipped and gave u a `Heads`**")
            await fliping.edit(content=f'{flip}')

#happy

    @commands.command(description='If you\'re happy send sp!happy' )
    @commands.guild_only()
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def happy(self, ctx):
        await ctx.send(f'https://media1.tenor.com/images/3419ea3da202cf42d6c7ab37a7fcd44e/tenor.gif')

#sad

    @commands.command(description='Don\'t be sad :)')
    @commands.guild_only()
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def sad(self, ctx):
        await ctx.send(f'https://media1.tenor.com/images/09b085a6b0b33a9a9c8529a3d2ee1914/tenor.gif')

#angry

    @commands.command(description='Someone\'s angry (><)')
    @commands.guild_only()
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def angry(self, ctx):
        await ctx.send(f'https://tenor.com/view/anime-angry-evil-plan-gif-14086662')

#f press

    @commands.command(description='Send sp!F to pay respects. ')
    @commands.guild_only()
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def f(self, ctx):
        # f in the chats bois 
        await ctx.send(f'{ctx.author.display_name} paid their respects.')

#calculate

    @commands.command(aliases = ["calculator"],description="Calculate BODMAS here :)")
    @commands.guild_only()
    @commands.cooldown(1, 15 ,commands.BucketType.user)
    # ever doubt yourself then clac your thoughts out 
    # this uses the in built eval of python to do things like DMAS
    async def calc(self, ctx, *, query : str = None):
        if query is None:
            await ctx.send("What to evaluate?")
        else:
            allowed = set('0123456789+-*/()')
            clean = ''.join(char for char in query if char in allowed)
            try:
                await ctx.send(f'``{query}`` ``=`` ``{eval(clean)}\n``')
            except Exception:
                await ctx.send('Please a write valid equation.')

# dice roll

    @commands.command(aliases=["dice", "diceroll"])
    @commands.guild_only()
    # ludo
    async def roll(self, ctx):
        responses = ['<:dice_1:820539955020824616>',
                        '<:dice_2:820540220205563914>',
                        '<:dice_3:820540440897650689>',
                        '<:dice_4:820540766614585345>',
                        '<:dice_5:820541148614885408>'
                        '<:dice_6:820541383911145492>']

        msg_1 = await ctx.send(f"** The Dice is Rolling Now**")
        msg_2 = await ctx.send(f"<a:dice_roll:820534048836550666>")

        await asyncio.sleep(8)

        await msg_1.edit(content=f"**The Dice has Roled on:**")
        await msg_2.edit(content=random.choice(responses))  

# rps

    @commands.command()
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def rps(self, ctx, msg: str):

        tie_data= ['Tie for this time but I am sure I will win the next time.', 'We have tied, a good battle.',
        'It was a good battle, learned alot from you but a tie is a tie', 'Good batlle, you didnnot disappoint me.']

        win_data= ['Sorry but I will be taking the crown for today.','Hehe, no victory for you today, friend. ',
         'A good match but you lost.', 'I have seen better from you.', 'Weakness disgusts me.', 'I see no god up here, other than me!' ]

        data = ['I have lost this time but it doesnot mean that this is over', 'I have lost, good battle.',
        'Never felt a defeat in so long.', 'Ah the smell of defeat, finally!', 'I have lost to a meer human',
        'Hey kid, you won but not for long.', 'I have lost this time but next time I will crush you!']

        t = ["rock", "paper", "scissors"]
        result = None
        tcolor = None
        computer = t[randint(0, 2)]
        player = msg.lower()

        if player == computer:
            result = tie_data

        elif player == "scissors":

            if computer == "rock":
                result=win_data
            else:
                result= data

        elif player == "rock":
            if computer == "paper":
               result= win_data
            else:
                result= data

        elif player == "paper":
            if computer == "scissors":
                result= win_data

            else:
                result= data
        else:
            await ctx.send("Do I have to teach you rock scissors and paper now?")

        if result==win_data:
            tcolor=0x2eff5d
        if result==data:
            tcolor=0xff0003
        if result ==tie_data:
            tcolor=0x529dff


        final_result= random.choice(result)
        embed= discord.Embed(color=tcolor,
                             title= f"Rock Paper Scissors")
        embed.set_thumbnail(url=f'https://media.tenor.com/images/5969d2658a51ef93de54a0049fffac9e/tenor.gif')
        embed.add_field(name="I choose:", value= f'**{computer}**' ,inline=True)

        embed.add_field(name=f"SPIKE's words:", value=f'"**{final_result}**"',inline=False)


        embed.set_footer(text=f'Played with {ctx.author}',icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

#pass

    @commands.command(name="password", aliases=['pass', 'generator', 'passwordgenerator'], description='Get Random Passwords Generated in your DMs')
    @commands.cooldown(rate=1, per=2.0, type=commands.BucketType.user)
    async def password(self, ctx, amt: int = 8):
        """ Get random password in DM  🔒"""
        try:
            nwpss = []
            lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                   'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '!', '@',
                   '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', ",", '}', ']',
                   '[', ';', ':', '<', '>', '?', '/', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '`', '~',
                   'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                   'U', 'V', 'W', 'X', 'Y', 'Z']
            for x in range(amt):
                newpass = random.choice(lst)
                nwpss.append(newpass)
            fnpss = ''.join(nwpss)
            await ctx.send(f'`{ctx.author}`, attempting to send you the genereated password in dms.')
            await ctx.author.send(f':white_check_mark: Password Generated: ```{fnpss}```')
        except Exception as e:
            print(e)

#slots command

    @commands.command(aliases=['slots', 'bet'], name='Slot')
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def slot(self, ctx):
        emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
        a = random.choice(emojis)
        b = random.choice(emojis)
        c = random.choice(emojis)

        slotmachine = f"**[ {a} | {b} | {c} ]\n{ctx.author.name}**,"

        if a == b == c:
            await ctx.send(embed=discord.Embed(title='Slot Machine:',
                                               description=slotmachine + ' has gotten 3/3 he wins!!! :tada:',
                                               colour=discord.Colour.red()))
        elif (a == b) or (a == c) or (b == c):
            await ctx.send(embed=discord.Embed(title='Slot Machine:',
                                               description=slotmachine + ' has gotten 2/3 he wins!!! :tada:',
                                               colour=discord.Colour.red()))
        else:
            await ctx.send(embed=discord.Embed(title='Slot Machine:',
                                               description=slotmachine + ' has gotten 0/3 he looses. :pensive:',
                                               colour=discord.Colour.red()))

#cheers COMMAND

    @commands.command(aliases=['cheers'])
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def beer(self, ctx, user: discord.Member = None, *, reason: commands.clean_content = ""):
        if not user or user.id == ctx.author.id:
            return await ctx.send(f"**{ctx.author.mention}**: fieeeeestaaa!🎉🍺")
        if user.bot:
            return await ctx.send(f"You that lonely? Give an actual person not a bot.")
        beer_offer = f"**{user.mention}**, You have a 🍺 offered from **{ctx.author.mention}**"
        beer_offer = beer_offer + f"\n\n**Reason:** {reason}" if reason else beer_offer
        msg = await ctx.send(beer_offer)

        def reaction_check(m):
            if m.message_id == msg.id and m.user_id == user.id and str(m.emoji) == "🍻":
                return True
            return False

        try:
            await msg.add_reaction("🍻")
            await self.bot.wait_for('raw_reaction_add', timeout=10.0, check=reaction_check)
            await msg.edit(content=f"**{user.mention}** and **{ctx.author.mention}** Are enjoying a lovely 🍻")
            await msg.clear_reactions()
        except asyncio.TimeoutError:
            await msg.delete()
            await ctx.send(f"Well, it seems **{user.name}** didn't wanted to say 'cheers' with **{ctx.author.name}** ;-;")
        except discord.Forbidden:
            beer_offer = f"{user.mention} and {ctx.author.mention} are enjoying a 🍻."
            beer_offer = beer_offer + f"\n\n**reason:** {reason}" if reason else beer_offer
            await msg.edit(content=beer_offer)

#simp COMMAND

    @commands.command(name='Simp')
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def simp(self, ctx, user: discord.Member = None):
        user = user or ctx.author
        embed = discord.Embed(
            color=discord.Color.red(),
            description=f'{user.display_name} is {random.randint(0, 101)}% simp'
        )
        await ctx.send(embed=embed)

#iq COMMAND

    @commands.command(name='IQ')
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def iq(self, ctx, user: discord.Member = None):
        user = user or ctx.author
        iq = ['130 and above (Very Superior)',
              '120–129 (Superior)',
              '110–119 (High Average)',
              '90–109 (Average)',
              '80–89 (Low Average)',
              '70–79 (Borderline)',
              '69 and below	(Extremely Low)']
        e = discord.Embed(
            color=discord.Colour.red(),
            description=f'{user.display_name} IQ is {random.choice(iq)}'
            )
        await ctx.send(embed=e)

#roast COMMAND

    @commands.command(aliases=['insult'], name='Roast')
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def roast(self, ctx, user: discord.Member=None):
        if not user:
            user = ctx.author
        A = ['You’re the reason God created the middle finger.',
             'You’re a grey sprinkle on a rainbow cupcake.',
             'If your brain was dynamite, there wouldn’t be enough to blow your hat off.',
             'You are more disappointing than an unsalted pretzel.',
             'Light travels faster than sound which is why you seemed bright until you spoke.',
             'We were happily married for one month, but unfortunately we’ve been married for 10 years.',
             'Your kid is so annoying, he makes his Happy Meal cry.',
             'You have so many gaps in your teeth it looks like your tongue is in jail.',
             'Your secrets are always safe with me. I never even listen when you tell me them.',
             'I’ll never forget the first time we met. But I’ll keep trying.',
             'I forgot the world revolves around you. My apologies, how silly of me.',
             'I only take you everywhere I go just so I don’t have to kiss you goodbye.',
             'Hold still. I’m trying to imagine you with personality.',
             'Our kid must have gotten his brain from you! I still have mine.',
             'Your face makes onions cry.',
             'The only way my husband would ever get hurt during an activity is if the TV exploded.',
             'You look so pretty. Not at all gross, today.',
             'Her teeth were so bad she could eat an apple through a fence.',
             'I’m not insulting you, I’m describing you.',
             'I’m not a nerd, I’m just smarter than you.',
             'Keep rolling your eyes, you might eventually find a brain.',
             'Your face is just fine but we’ll have to put a bag over that personality.',
             'You bring everyone so much joy, when you leave the room.',
             'I thought of you today. It reminded me to take out the trash.',
             'Don’t worry about me. Worry about your eyebrows.',
             'there is approximately 1,010,030 words in the language english, but i cannot string enough words together to express how much i want to hit you with a chair']
        await ctx.send(embed=discord.Embed(
            colour=discord.Colour.red(),
            description=f'`{user.display_name}`,\n {random.choice(A)}'
        ).set_author(name=self.bot.user.display_name, icon_url=self.bot.user.avatar_url))

#kill COMMAND

    @commands.command(aliases=['murder', 'die'], name='Kill')
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def kill(self, ctx, *, user: discord.Member = None):
        user = user or ctx.author
        died = ['rolling out of the bed and the demon under the bed ate them.',
                'getting impaled on the bill of a swordfish.',
                'falling off a ladder and landing head first in a water bucket.',
                'his own explosive while trying to steal from a condom dispenser.',
                'a coconut falling off a tree and smashing there skull in.',
                'taking a selfie with a loaded handgun shot himself in the throat.',
                'shooting himself to death with gun carried in his breast pocket.',
                'getting crushed while moving a fridge freezer.',
                'getting crushed by his own coffins.',
                'getting crushed by your partner.',
                'laughing so hard at The Goodies Ecky Thump episode that he died of heart failure.',
                'getting run over by his own vehicle.',
                'car engine bonnet shutting on there head.',
                'tried to brake check a train.',
                'dressing up as a cookie and cookie monster ate them.',
                'trying to re-act Indiana Jones, died from a snake bite.',
                'tried to short circuit me, not that easy retard',
                'tried to fight a bear with there hands',
                'getting Billy Heartied in the ball sacks'
                ]
        await ctx.send(embed=discord.Embed(
            colour=discord.Colour.red(),
            description='{} was killed by {}'.format(user.display_name, random.choice(died))
        ).set_author(name=self.bot.user.display_name, icon_url=self.bot.user.avatar_url))


# setup COMMAND


def setup(bot):
    bot.add_cog(Fun(bot))
    print("Fun Cog is Loaded!")
