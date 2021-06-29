import io
import discord
import praw
from discord.ext import commands, tasks
import datetime
import random
import asyncio
import traceback
import aiohttp
from aiohttp import ClientSession
from aiohttp import ClientSession
from PIL import Image,ImageDraw,ImageFont
from io import BytesIO
import requests
import urllib
from discord.ext.commands import command, cooldown
import json
import sys

class Api(commands.Cog, name='Api'):

    def __init__(self,bot):
        self.bot = bot

    @commands.command(description='Get quick info about an API')
    @commands.guild_only()
    async def api(self, ctx, *, url=None):
        if url == None:
            return await ctx.send("Please pass in an URL")
        else:
            req = requests.get(f"{url}").json()
            req_1= json.dumps(req,indent=4)
            embed = discord.Embed(color = self.bot.color, timestamp=datetime.datetime.utcnow())
            embed.set_author(name="API response to ", url=f"{url}", icon_url=ctx.me.avatar_url)
            embed.description=f"```json\n{req_1}```"
            embed.set_footer(text=f"Requested by {ctx.author}")
            await ctx.send(embed=embed)




    @commands.command()
    @commands.guild_only()
    async def help_api(self, ctx):
        embed= discord.Embed(title='Image commands or API commands ||commands have cooldowns||', colour=random.choice(self.bot.color_list))
        embed.set_author(name="SPIKE", icon_url=f'{ctx.me.avatar_url}')
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.add_field(name="cat", value=  f' Make SPIKE send a meow picture ', inline=False)
        embed.add_field(name="catfact", value=  f' Make SPIKE send a meowy fact about cats ', inline=False)
        embed.add_field(name="dog", value=   f' Make SPIKE send a woof picture ', inline=False)
        embed.add_field(name="dogfact", value=  f' Make SPIKE send a woofy fact about dogs ', inline=False)
        embed.add_field(name="panda", value= f' Make SPIKE send cutest pandas', inline=False)
        embed.add_field(name="koala", value=f'Make SPIKE send a cozy, warmth pic of the lazy but cute animal')
        embed.add_field(name="pandafact", value=  f' Make SPIKE send a cutie fact about the Pandas', inline=False)
        embed.add_field(name="pikachu", value= f' Make SPIKE send a pikachu gif or an image', inline=False)
        embed.add_field(name="yearfact", value= f' Make SPIKE send a random fact on the mentioned year', inline=False)
        embed.add_field(name="clyde", value= f' Make clyde say something', inline=False)


        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url= ctx.author.avatar_url)
        await ctx.send(embed=embed)





    @commands.command(description='Sends a random doggo picture.')
    @commands.guild_only()
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def dog(self, ctx):
        try:
            async with ctx.channel.typing():
                async with aiohttp.ClientSession() as cs:
                    async with cs.get("https://dog.ceo/api/breeds/image/random") as r:
                        data = await r.json()

                        embed = discord.Embed(title="Woof", colour=random.choice(self.bot.color_list))
                        embed.set_image(url=data['message'])
                        embed.set_footer(text=f"Requested by {ctx.author}, Source: Thedogapi", icon_url=ctx.author.avatar_url)

                        await ctx.send(embed=embed)
        except:
                await ctx.send(f'Command on cooldown for some seconds.', delete_after=5)


    @commands.command(description='Echos\' words from clyde')
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def clyde(self, ctx, *, text):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://nekobot.xyz/api/imagegen?type=clyde&text={text}") as r:
                res = await r.json()
                embed = discord.Embed(
                    color=random.choice(self.bot.color_list)

                )
                embed.set_image(url=res['message'])
                embed.set_footer(text=f'Requested by {ctx.author.name}, Source : Nekobot.xyz',icon_url=ctx.author.avatar_url)

                await ctx.send(embed=embed)
                await ctx.message.delete()


    @commands.command(description='Sends a random year fact.')
    @commands.guild_only()
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def yearfact (self, ctx):

        async with aiohttp.ClientSession() as cs:

            async with cs.get(f"http://numbersapi.com/random/year?json") as r:
                data = await r.json()

                embed = discord.Embed(title= data['number'], description=data['text'], colour=random.choice(self.bot.color_list))

                embed.set_footer(text=f"Requested by {ctx.author}, Fact from numbersapi.com", icon_url=ctx.author.avatar_url)
                await ctx.send(embed=embed)


    @commands.command(description='Sends a random panda fact :heart:')
    @commands.guild_only()
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def pandafact(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs:
                async with cs.get("https://some-random-api.ml/facts/panda") as r:
                    data = await r.json()

                    embed = discord.Embed(title="Panda fact", colour=random.choice(self.bot.color_list))
                    embed.set_author(name=data['fact'])
                    embed.set_footer(text=f"Requested by {ctx.author}, Source: Some-random-api", icon_url=ctx.author.avatar_url)

                    await ctx.send(embed=embed)


    @commands.command(description='Sends a random cat picture.')
    @commands.guild_only()
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def catfact(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs:
                async with cs.get("https://some-random-api.ml/facts/cat") as r:
                 data= await r.json()

                 embed = discord.Embed(title="Cat fact :D", colour=random.choice(self.bot.color_list))
                 embed.set_author (name=data['fact'])
                 embed.set_footer(text=f"Requested by {ctx.author}, Source : Some-random-api", icon_url=ctx.author.avatar_url)
                 await ctx.send(embed=embed)


    @commands.command(description='Sends a random doggo fact.')
    @commands.guild_only()
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def dogfact(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs:
                async with cs.get("https://some-random-api.ml/facts/dog") as r:
                 data= await r.json()

                 embed = discord.Embed(title="Dog fact :D", colour=random.choice(self.bot.color_list))
                 embed.set_author (name=data['fact'])
                 embed.set_footer(text=f"Requested by {ctx.author}, Source : Some-random-api", icon_url=ctx.author.avatar_url)

                 await ctx.send(embed=embed)


    @commands.command(description='Sends a random kitty picture.')
    @commands.guild_only()
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def cat(self, ctx):

            async with aiohttp.ClientSession() as cs:
                async with cs.get("http://aws.random.cat/meow") as r:
                    data = await r.json()

                    embed = discord.Embed(title="Meow", colour=random.choice(self.bot.color_list))
                    embed.set_image(url=data['file'])
                    embed.set_footer(text=f"Requested by {ctx.author}, source : Aws.randam.cat/meow", icon_url=ctx.author.avatar_url)

                    await ctx.send(embed=embed)


    @commands.command(description='Sends a random panda picture :heart:')
    @commands.guild_only()
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def panda(self, ctx):

            async with aiohttp.ClientSession() as cs:
                async with cs.get("https://some-random-api.ml/img/panda") as r:
                    data = await r.json()

                    embed = discord.Embed(title="Pandasound :P", colour=random.choice(self.bot.color_list))
                    embed.set_image(url=data['link'])
                    embed.set_footer(text=f"Requested by {ctx.author}, Source : Some-random-api", icon_url=ctx.author.avatar_url)

                    await ctx.send(embed=embed)

    @commands.command(description='Nevermind the koala is sleeping.')
    @commands.guild_only()
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def koala(self, ctx):

            async with aiohttp.ClientSession() as cs:
                async with cs.get("https://some-random-api.ml/img/koala") as r:
                    data = await r.json()

                    embed = discord.Embed(title="Koala sound :P", colour=random.choice(self.bot.color_list))
                    embed.set_image(url=data['link'])
                    embed.set_footer(text=f"Requested by {ctx.author}, Source : Some-random-api", icon_url=ctx.author.avatar_url)

                    await ctx.send(embed=embed)



    @commands.command(description='*Pikachu open mouth*')
    @commands.guild_only()
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def pikachu(self,ctx):

            async with aiohttp.ClientSession() as cs:
                async with cs.get("https://some-random-api.ml/img/pikachu") as r:
                    data = await r.json()

                    embed = discord.Embed(title="Pika Pika" ,colour=random.choice(self.bot.color_list))
                    embed.set_image(url=data['link'])
                    embed.set_footer(text=f"Requested by {ctx.author}, SOURCE :-  Some Random Api", icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=embed)



    @commands.command(description='Sends a random numberfact.')
    @commands.guild_only()
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def numberfact(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"http://numbersapi.com/random?json") as r:
                data = await r.json()

                embed = discord.Embed(title=data['number'], description=data ['text'],colour=random.choice(self.bot.color_list))
                embed.set_footer(text=f"Requested by {ctx.author}, Fact from numbersapi.com", icon_url=ctx.author.avatar_url)
                await ctx.send(embed=embed)


    @commands.command(description='Advices for you.')
    @commands.guild_only()
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def advice(self, ctx):
        r = requests.get("https://api.adviceslip.com/advice").json()
        advice= r["slip"]["advice"]
        embed = discord.Embed(title=advice ,colour=random.choice(self.bot.color_list))
        embed.set_footer(text=f"Requested by {ctx.author}, adviceslip.com", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)




    @commands.command(description='Anime quotes :)')
    @commands.guild_only()
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def aquote(self, ctx):
       async with aiohttp.ClientSession() as cs:
           async with cs.get(f'https://some-random-api.ml/animu/quote') as r:

                data = await r.json()
                by = data['characther']
                anime= data['anime']
                quote= data['sentence']

                embed = discord.Embed(title=f'"{quote}"', colour=random.choice(self.bot.color_list))
                embed.set_author(name=f'By {by} from {anime}')
                embed.set_footer(text=f'Requested by {ctx.author}, Quote from some-random-api')
                await ctx.send(embed=embed)

    @commands.command(description='Give a headpat to someone.')
    @commands.guild_only()
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def headpat(self,ctx):

            async with aiohttp.ClientSession() as cs:
                async with cs.get("https://some-random-api.ml/animu/pat") as r:
                    data = await r.json()

                    embed = discord.Embed(title="There there everything will be better" ,colour=random.choice(self.bot.color_list))
                    embed.set_image(url=data['link'])
                    embed.set_footer(text=f"Requested by {ctx.author}, SOURCE :-  Some Random Api", icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=embed)

    @commands.command(description=';)')
    @commands.guild_only()
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def wink(self,ctx):

            async with aiohttp.ClientSession() as cs:
                async with cs.get("https://some-random-api.ml/animu/wink") as r:
                    data = await r.json()

                    embed = discord.Embed(title=";)" ,colour=random.choice(self.bot.color_list))
                    embed.set_image(url=data['link'])
                    embed.set_footer(text=f"Requested by {ctx.author}, SOURCE :-  Some Random Api", icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=embed)

    @commands.command(description='Huggggggggggg.....')
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def hug(self,ctx):

            async with aiohttp.ClientSession() as cs:
                async with cs.get("https://some-random-api.ml/animu/hug") as r:
                    data = await r.json()

                    embed = discord.Embed(title="Hug!!!!!" ,colour=random.choice(self.bot.color_list))
                    embed.set_image(url=data['link'])
                    embed.set_footer(text=f"Requested by {ctx.author}, SOURCE :-  Some Random Api", icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=embed)

    @commands.command(description='Palm to the face')
    @commands.guild_only()
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def facepalm(self,ctx):

            async with aiohttp.ClientSession() as cs:
                async with cs.get("https://some-random-api.ml/animu/face-palm") as r:
                    data = await r.json()

                    embed = discord.Embed(title="Palm to the face" ,colour=random.choice(self.bot.color_list))
                    embed.set_image(url=data['link'])
                    embed.set_footer(text=f"Requested by {ctx.author}, SOURCE :-  Some Random Api", icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=embed)

    @commands.command(description='Defines most of the words out there', aliases=['meaning', 'define'])
    @commands.guild_only()
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def dictionary(self, ctx, *, word:str):
        try:
            url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
            data = requests.get(url).json()
            definition = (data[0]['meanings'][0]['definitions'][0]['definition'])
            example = (data[0]['meanings'][0]['definitions'][0]['example'])
            text = data[0]['phonetics'][0]['text']
            audio = data[0]['phonetics'][0]['audio']
            embed = discord.Embed(color = random.choice(self.bot.color_list))
            #embed.set_author(name=f"{word}")
            #embed.add_field(name="Phonetics", value=f"Text = {text} \n[Audio]({audio})")
            embed.add_field(name="Definition", value=f"{definition}", inline=False)
            embed.add_field(name="Example", value = f"{example}", inline=False)
            await ctx.send(embed=embed)
        except KeyError:
            await ctx.send(f"**Sorry! Couldn't Find enough information about the word `{word}`**")

    @commands.command()
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def meme(self, ctx):

        r = requests.get("https://memes.blademaker.tv/api?lang=en")
        res = r.json()
        
        title = res['title']
        ups = res["ups"]
        downs = res["downs"]
        sub = res["subreddit"]

        m = discord.Embed(title=f"{title}", description=f"```Subreddit : r/{sub}```", color = random.choice(self.bot.color_list))
        m.set_image(url = res["image"])
        m.set_footer(text=f"👍: {ups} | 👎: {downs}\n Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=m)

# joke COMMAND

    @commands.command(aliases=['jokes'], name='Joke')
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def joke(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    'https://sv443.net/jokeapi/v2/joke/Miscellaneous?blacklistFlags=nsfw,religious,political,racist,sexist&type=twopart') as r:
                r = await r.json()
        embed = discord.Embed(title=f"Joke", description=f"{r['setup']}\n {r['delivery']}", colour=random.randint(0x000000, 0xFFFFFF), timestamp=datetime.datetime.utcnow())
        # embed.add_field(name='Setup:', value=r['setup'])
        # embed.add_field(name='Delivery:', value=r['delivery'], inline=False)
        embed.set_footer(text='Prompted by {}'.format(ctx.author), icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

#triggered pic CMD

    @commands.command()
    async def triggered(self, ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author
        await ctx.trigger_typing()
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://some-random-api.ml/canvas/triggered?avatar={member.avatar_url_as(format="png")}') as af:
                if 300 > af.status >= 200:
                    fp = io.BytesIO (await af.read())
                    file = discord.File(fp, "triggered.png")
                    em = discord.Embed(title="", color=ctx.author.color)
                    em.set_image(url="attachment://triggered.png")
                    await ctx.send(embed=em, file=file)


def setup(bot):
    bot.add_cog(Api(bot))
    print("Api cog is Working!")

#👍: {ups} | 👎: {downs} 
