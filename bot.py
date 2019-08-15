import datetime
import asyncio
import discord
from discord.ext import commands
from os import getenv

description = 'Bot para mandar alertas dos boss do servidor South America'
bot = commands.Bot(command_prefix='.', description=description)
token = getenv('BOT_TOKEN')

@bot.event
async def on_ready():
	print('Bot ID: ', bot.user.id)
	print('Bot name: ', bot.user.name)
	print('---------------')
	print('This bot is ready for action!')
	print('I\'m currently on those servers: ')
	for guild in bot.guilds:
		print(guild)

@bot.command()
async def peixinho(ctx):
	'''glub! '''
	await ctx.send('_glub glub_')

@bot.command()
async def notifyme(ctx):
	'''Adiciona seu nome na lista de avisos'''
	user = ctx.message.author
	role = discord.utils.get(ctx.guild.roles.roles, name='Boss Timer')
	await user.add_roles()
	await ctx.send('Você será notificado na hora de um boss :)')

@bot.command()
async def removeme(ctx):
	'''Remove seu nome da lista de avisos'''
	user = ctx.message.author
	role = discord.utils.get(ctx.guild.roles.roles, name='Boss Timer')
	await user.remove_roles()
	await ctx.send('Você **não será mais** notificado na hora de um boss :)')

@bot.event
async def background_task():
	await bot.wait_until_ready()
	while not bot.is_closed():
		print('1 minute counter')
		await asyncio.sleep(60) # task runs every 60 seconds

bot.bg_task = bot.loop.create_task(background_task())

bot.run(token)