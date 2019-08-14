import datetime
import discord
import pymongo
from os import getenv
from discord.ext import commands

description = 'Bot para mandar alertas dos boss do servidor South America'
bot = commands.Bot(command_prefix='!', description=description)
token = getenv('BOT_TOKEN')
uri = getenv('MONGODB_URI')

# client = pymongo.MongoClient(uri)
# db = client.get_default_database()

@bot.event
async def on_ready():
    print('Bot ID: ', bot.user.id)
    print('Bot name: ', bot.user.name)
    print('---------------')
    print('This bot is ready for action!')

@bot.command(pass_context=True)
async def ping(ctx):
    '''Returns pong when called'''
    author = ctx.message.author.name
    server = ctx.message.server.name
    await bot.say('Pong for {} from {}!'.format(author, server))

@bot.command(pass_context=False)
async def peixinho():
	'''glub! '''
	await bot.say('_glub glub_')


bot.run(token)