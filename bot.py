import discord
from discord.ext.commands import Bot
from discord import Intents
intents = Intents.all()

bot = Bot(command_prefix='$')

@bot.event
async def on_ready():
	print(f'Bot connected as {bot.user}')
	
@bot.event
async def on_message(message):
	if message.content == 'komunizm':
		await message.channel.send('@Magneter#5065')

@bot.event
async def on_message(message):
	if message.content == 'kapitalizm':
		await message.channel.send('@Magneter#5065')
		

bot.run('NzQ4ODQwMjY2MDQyOTY2MDU3.X0jR2A.Bjy6r4Xvom6Zi8C0W_qyl-vWR-s')

