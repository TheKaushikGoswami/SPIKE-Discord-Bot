import discord
from discord.ext import commands
import sys
import datetime
import random
import time
from ago import human
import collections
import discord.utils

class Utility(commands.Cog, name='Moderation'):

    def __init__(self,bot):
        self.bot = bot

#suggestion CMD
                    
    @commands.command()
    async def suggest(self,ctx, *, message):
        guild = ctx.guild
        s=discord.Embed(title="SUGGESTION",description=f"{message}", color = 0xE67E22)
        s.set_thumbnail(url=f"https://www.harveynorman.com.au/blog/assets/Earth-Hour-845x1000.jpg")
        s.set_footer(text=f"Suggested by {ctx.author}", icon_url=ctx.author.avatar_url)
        channel = discord.utils.get(guild.text_channels, name='suggestion')
        msg=await channel.send(embed=s)
        await msg.add_reaction("✅")
        await msg.add_reaction("❌")
        await ctx.send(f"**✅ Success! Your suggestion has been sent successfully**")

#whois CMD

    @commands.command(aliases=['whois', 'ui'], description='To see information of a user.')
    @commands.guild_only()
    async def userinfo(self,ctx, member: discord.Member=None):

        member = member or ctx.author
        guild = ctx.guild
        # ignore the guild check haha it's for the main server :vein_shy:
        '''
        if ctx.guild.id != (guild):
            uroles = []
            # loops through to get the roles and slickes the @everyone role 
            for role in member.roles[1:]:
                if role.is_default():
                    continue
                uroles.append(role.mention)

                uroles.reverse()
            # would suggest the ago module like how i have 
            time = member.created_at
            time1= member.joined_at

            embed=discord.Embed(color=random.choice(self.bot.color_list), timestamp=ctx.message.created_at, type="rich")
            embed.set_thumbnail(url= f"{member.avatar_url}")
            embed.set_author(name=f"{member.name}'s information",icon_url=f'{ctx.me.avatar_url}')
            embed.add_field(name="ㅤ",value=f'**Nickname:** `{member.display_name}`\n\n'
                                                            f'**ID** {member.id}\n\n'
                                                            f'**Account created:** {human(time, 4)}\n\n'
                                                            f'**Server joined at:** {human(time1, 3)}\n\n'
                                                            f'**Role(s):** {", ".join(uroles)}\n\n'
                                                            f'**Highest role:** {member.top_role.mention}'
                                                             , inline=False)

            embed.set_footer(text=f"Requested by {ctx.author}",  icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        
        elif ctx.guild.id == guild:
        '''
        member_id= str(member.id)
        uroles = []
        for role in member.roles[1:]:
            if role.is_default():
                continue
            uroles.append(role.mention)

            uroles.reverse()
        timestamp = 'ㅤ'
        time = member.created_at
        time1= member.joined_at
        if member.status == discord.Status.online:
            status= '<:OnlineStatus:796628774002098187>'
        elif member.status == discord.Status.idle:
            status= '<a:IdleStatus:796629237565620234>'
        elif member.status== discord.Status.dnd:
            status = '<a:DNDStatus:796629229193789440>'
        else:
            status = '<:OfflineStatus:796628779216011275>'
        if member.activity == None:
            activity = 'None'
        else:
            activity = member.activities[-1].name
            try:
                timestamp = member.activities[0].details
            except:
                timestamp ='ㅤ'
        embed=discord.Embed(color=random.choice(self.bot.color_list), timestamp=ctx.message.created_at, type="rich")
        embed.set_thumbnail(url= f"{member.avatar_url}")
        embed.set_author(name=f"{member.name}'s information",icon_url=f'{ctx.me.avatar_url}')
        embed.add_field(name="__General information__",value=f'**Nickname :** `{member.display_name}`\n'
                                                        f'**ID :** {member.id}\n'
                                                        f'**Account created :** {human(time, 4)}\n'
                                                        f'**Server joined :** {human(time1, 3)}\n'
                                                        ,inline=False)
        
        embed.add_field(name="__Role info__", value= f'**Highest role :** {member.top_role.mention}\n'
                                                    f'**Color** : {member.color}\n'
                                                    f'**Role(s) :** {", ".join(uroles)}\n'
                                           , inline=False)
                                               
        embed.add_field(name="__Presence__", value =f'**Status : ** {status}\n'
                                                    f'**Activity : ** ```{activity}:  \nㅤ{timestamp}```')
        embed.set_footer(text=f"Requested by {ctx.author.name}",  icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
        return


#avatar cmd
    @commands.command(aliases=['av'])
    @commands.guild_only()
    async def avatar(self, ctx,*, user: discord.Member=None):
        # user as the mention
        if not user:
            user = ctx.author
            # self-explainatory
        embed = discord.Embed( title=f"{user.name}'s avatar",color=random.choice(self.bot.color_list))
        embed.description = f'[PNG]({user.avatar_url_as(format="png")}) | [JPEG]({user.avatar_url_as(format="jpeg")}) | [WEBP]({user.avatar_url_as(format="webp")})'
        embed.set_image(url=str(user.avatar_url_as(format='png')))
        embed.set_footer(text=f"Requested by {ctx.author}",  icon_url=ctx.author.avatar_url)
        # Nitro users :Eyes:
        if user.is_avatar_animated():
            embed.description += f' | [GIF]({user.avatar_url_as(format="gif")})'
            embed.set_image(url=str(user.avatar_url_as(format='gif')))


        return await ctx.send(embed=embed)

#membercount
    @commands.command(aliases=['servercount','membercount'], description='Count the total number of users on the server.')
    @commands.guild_only()
    async def members(self,ctx):
        # get the total no of members of a server
        embed=discord.Embed(color=0x529dff)
        embed.add_field(name="Total members", value=f"{ctx.guild.member_count}", inline=False)
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)

#serverinfo
    @commands.command(aliases=['si'], description='To get the server information.')
    @commands.guild_only()
    # a cool server info command gets most of the basic things you would need to know about a server :)
    async def serverinfo(self, ctx):


        if ctx.channel.id ==757108786497585172:
            return

        guild= ctx.guild
        emojis = str(len(guild.emojis))

        channels = str(len(guild.channels))
        roles= str(len(guild.roles))
        time= ctx.guild.created_at.strftime("%a, %#d %B %Y, %I:%M %p ")
        voice= str(len(guild.voice_channels))
        text= str(len(guild.text_channels))
        statuses = collections.Counter([member.status for member in guild.members])

        online = statuses[discord.Status.online]
        idel = statuses[discord.Status.idle]
        dnd = statuses[discord.Status.dnd]
        offline= statuses[discord.Status.offline]

        embed= discord.Embed(
                                timestamp= ctx.message.created_at, color=random.choice(self.bot.color_list) )

        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.set_author(name=f"Information for  {ctx.guild.name}")
        embed.add_field(name="__General information__\n", value= f'**Server name : ** {guild.name}\n'
                                                               f'**Server region : ** {guild.region}\n'
                                                               f'**Server ID : ** {guild.id}\n'
                                                               f'**Created at : ** {time}\n'
                                                               f'**Verification level : ** {guild.verification_level} \n'
                                                               f'**Server owner : ** <@{ctx.guild.owner_id}> \n', inline=False)


        embed.add_field(name="\n\n\n__Statistics__", value= f'**Member count : ** {ctx.guild.member_count}\n'
                                                 f'**Role count : ** {roles} \n'
                                                 f'**Channel count : ** {channels}\n'
                                                 f'**Text channels :** {text}\n'
                                                 f'**Voice channels :** {voice}\n'
                                                 f'**Emoji count : ** {emojis}\n'
                                                 f'**Server boosts : ** {guild.premium_subscription_count}\n')

        embed.add_field(name="__Activity__", value= f'<:OnlineStatus:796628774002098187>{online}\n'
                                                    f'<a:IdleStatus:796629237565620234>{idel}\n'
                                                    f'<a:DNDStatus:796629229193789440>{dnd}\n'
                                                    f'<:OfflineStatus:796628779216011275>{offline}')


        embed.set_footer(text=f"Requested by {ctx.author}",  icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

#role info COMMAND

    @commands.command(aliases=['rinfo'])
    @commands.has_permissions(manage_roles=True)
    async def roleinfo(self, ctx, *, rolename):
        allowed = []
        try:
            role = discord.utils.get(ctx.message.guild.roles, name=rolename)
            permissions = role.permissions

            for name, value in permissions:
                if value:
                    name = name.replace('_', ' ').replace(
                        'guild', 'server').title()
                    allowed.append(name)
        except:
            return await ctx.send(f"Couldn't find the role")
        time = role.created_at
        em = discord.Embed(description=f'', color=random.choice(self.bot.color_list), timestamp=time)
        em.set_author(name=f'{rolename}')
        em.set_thumbnail(url=f'{ctx.guild.icon_url}')
        em.add_field(name='__Info__', value=f'**ID :** {str(role.id)} \n'
                                            f'**Color :** {role.color}\n'
                                            f'**Hoisted :** {str(role.hoist)}\n'
                                            f'**Position :** {str(role.position)}\n'
                                            f'**Is mentionable :** {str(role.mentionable)}\n'
                                            f'**Members in role :** {str(len(role.members))}\n')
        em.add_field(name='__Role Permissions__',
                     value=f', '.join(allowed), inline=False)
        em.set_footer(text="Role created on")
        await ctx.send(embed=em)

#channel stats
    @commands.command(hidden=True, aliases=['cstats'])
    @commands.guild_only()
    @commands.has_permissions(kick_members=True)
    async def channelstats(self, ctx):
        channel = ctx.channel
        tmembers = str(len(channel.members))
        nsfw = (ctx.channel.is_nsfw())
        news = (ctx.channel.is_news())
        embed = discord.Embed(color=random.choice(self.bot.color_list))
        embed.set_thumbnail(url=f'{ctx.guild.icon_url}')
        embed.add_field(name="__Information__", value=f'**Server name: ** {ctx.guild.name} \n'
                        f'**Channel name :** {channel.name}\n'
                        f'**Channel ID : ** {channel.id} \n'
                        f'**Channel type : **{channel.type}\n'
                        f'**Channel category : ** {channel.category}\n'
                        f'**Topic : ** {channel.topic}\n'
                        f'**Channel position :** {channel.position}\n'
                        f'**Created at :** {channel.created_at.strftime("%a, %#d %B %Y, %I:%M %p ")}\n'
                        f'**Slowmode :** {channel.slowmode_delay}\n'
                        f'**Channel Permissions :** {channel.permissions_synced}\n'
                        f'**Channel members :** {tmembers}\n'
                        f'**Is nsfw : ** {nsfw}\n'
                        f'**Is news : ** {news}', inline=False)

        embed.set_author(name="SPIKE", icon_url=f'{ctx.me.avatar_url}')
        embed.set_footer(
            text=f" Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)

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

#poll CMD

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def poll(self, ctx, question, option1=None, option2=None):
        if option1==None and option2==None:
            await ctx.channel.purge(limit=1)
            message = await ctx.send(f"```New poll: \n{question}```\n**✅ = Yes**\n**❎ = No**")
            await message.add_reaction('❎')
            await message.add_reaction('✅')
        elif option1==None:
            await ctx.channel.purge(limit=1)
            message = await ctx.send(f"```New poll: \n{question}```\n**✅ = {option1}**\n**❎ = No**")
            await message.add_reaction('❎')
            await message.add_reaction('✅')
        elif option2==None:
            await ctx.channel.purge(limit=1)
            message = await ctx.send(f"```New poll: \n{question}```\n**✅ = Yes**\n**❎ = {option2}**")
            await message.add_reaction('❎')
            await message.add_reaction('✅')
        else:
            await ctx.channel.purge(limit=1)
            message = await ctx.send(f"```New poll: \n{question}```\n**✅ = {option1}**\n**❎ = {option2}**")
            await message.add_reaction('❎')
            await message.add_reaction('✅')

#setup COMMAND

def setup(bot):
    bot.add_cog(Utility(bot))
    print("Utility Cog is Loaded!")
