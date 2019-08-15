import datetime
import discord
from os import getenv
from discord.ext import commands

description = 'Bot para mandar alertas dos boss do servidor South America'
bot = commands.Bot(command_prefix='.', description=description)
token = getenv('BOT_TOKEN')

@bot.event
async def on_ready():
    print('Bot ID: ', bot.user.id)
    print('Bot name: ', bot.user.name)
    print('---------------')
    print('This bot is ready for action!')

@bot.command()
async def peixinho(ctx):
	'''glub! '''
	await ctx.send('_glub glub_')

@bot.command()
async def notifyme(ctx):
	'''Adiciona seu nome na lista de avisos'''
	role = discord.utils.get(ctx.guild.roles, name='Boss Timer')
	user = ctx.message.author
	await user.add_roles(role)
	await ctx.send('Você será notificado na hora de um boss :)')

@bot.command()
async def removeme(ctx):
	'''Remove seu nome da lista de avisos'''
	role = discord.utils.get(ctx.guild.roles, name='Boss Timer')
	user = ctx.message.author
	await user.remove_roles(role)
	await ctx.send('Você **não será mais** notificado na hora de um boss :)')

bot.run(token)