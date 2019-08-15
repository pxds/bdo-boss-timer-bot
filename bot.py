import datetime
import discord
from os import getenv
from discord.ext import commands

description = 'Bot para mandar alertas dos boss do servidor South America'
bot = commands.Bot(command_prefix='.', description=description)
client = discord.Client()
token = getenv('BOT_TOKEN')

# bt_role = discord.utils.get(client.get_guild().roles, name='Boss Timer')

@client.event
async def on_ready():
    print('Bot ID: ', bot.user.id)
    print('Bot name: ', bot.user.name)
    print('---------------')
    print('This bot is ready for action!')
    for guild in client.guilds:
    	print(guild)
    	pass

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

boss_about2_spawn == True

if boss_about2_spawn:
	channel.send("one shot one kill")
	boss_about2_spawn = False
	pass

bot.run(token)