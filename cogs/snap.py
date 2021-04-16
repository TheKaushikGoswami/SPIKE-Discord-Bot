from discord.ext import commands
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import discord
from datetime import datetime
import os
import sys
import asyncio

class snap(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def snap(self, ctx, member: discord.Member, *, message):
		colour = {
			"time": (114, 118, 125),
			"content": (220, 221, 222)
		}

		size = {
			"title": 20,
			"time": 13
		}

		font = 'fonts/Whitney-Medium.ttf'

		if not member:
			member = ctx.author

		img = Image.new('RGB', (500, 115), color = (54,57,63))
		titlefnt = ImageFont.truetype(font, size["title"])
		timefnt = ImageFont.truetype(font, size["time"])
		d = ImageDraw.Draw(img)
		if member.nick is None:
			txt = member.name
		else:
			txt = member.nick
		color = member.color.to_rgb()
		if color == (0, 0, 0):
			color = (255,255,255)
		d.text((90, 20), txt, font=titlefnt, fill=color)
		h, w = d.textsize(txt, font=titlefnt)
		time = datetime.utcnow().strftime("Today at %I:%M %p")
		d.text((90+h+10, 25), time, font=timefnt, fill=colour["time"])
		d.text((90, 25+w), message, font=titlefnt, fill=colour["content"])

		img.save('img.png')
		if member.is_avatar_animated():
			await member.avatar_url_as().save("pfp.gif")
			f2 = Image.open("pfp.gif")
		else:
			await member.avatar_url_as().save("pfp.png")
			f2 = Image.open("pfp.png")
		f1 = Image.open("img.png")
		f2.thumbnail((50, 55))
		f2.save("pfp.png")

		f2 = Image.open("pfp.png").convert("RGB")

		mask = Image.new("L", f2.size, 0)
		draw = ImageDraw.Draw(mask)
		draw.ellipse((0, 0, f2.size[0], f2.size[1]), fill=255)
		mask = mask.filter(ImageFilter.GaussianBlur(0))

		result = f2.copy()
		result.putalpha(mask)

		result.save('pfp.png')

		f2 = Image.open("pfp.png")

		f3 = f1.copy()
		f3.paste(f2, (20, 20), f2)
		f3.save("img.png")

		file = discord.File("img.png")
		await ctx.send(file=file)

		try:
			os.remove("pfp.gif")
			os.remove("pfp.png")
			os.remove("img.png")
			await ctx.message.delete()
		except:
			pass

def setup(bot):
    bot.add_cog(snap(bot))
    print("Snap cog is Working!")