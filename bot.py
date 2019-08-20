import datetime
import io
import asyncio
import discord
from discord.ext import commands
from os import getenv

async def print_boss_message(boss_name,boss_time,channel):
	if len(boss_name) == 1:
		await channel.send('{boss[0]} vai nascer em 5min'.format(boss=boss_name))
	elif len(boss_name) == 2:
		await channel.send('{boss[0]} e {boss[1]} vão nascer em 5min'.format(boss=boss_name))

async def print_next_boss_message(boss_name,boss_time,channel):
	if len(boss_name) == 1:
		await channel.send('O próximo boss será {boss[0].mention} às {time}'.format(boss=boss_name, time=boss_time))
	elif len(boss_name) == 2:
		await channel.send('Os próximos bosses são {boss[0].mention} e {boss[1].mention} às {time}'.format(boss=boss_name,time=boss_time))

file = io.open("boss_schedule.txt","r").read()
boss_schedule = eval(file)

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
	role = discord.utils.get(ctx.guild.roles, name='Boss Timer')
	await user.add_roles(role)
	await ctx.send('Você será notificado na hora de um boss :)')

@bot.command()
async def removeme(ctx):
	'''Remove seu nome da lista de avisos'''
	user = ctx.message.author
	role = discord.utils.get(ctx.guild.roles, name='Boss Timer')
	await user.remove_roles(role)
	await ctx.send('Você **não será mais** notificado na hora de um boss :(')

@bot.command()
async def setchannel(ctx):
	'''Define qual o canal que o bot irá enviar as mensagens'''
	channel = ctx.message.channel
	guild = ctx.message.guild
	bot.bg_task = bot.loop.create_task(background_task(channel,guild))
	await ctx.send('Vou realizar minhas notificações no canal {0.mention}'.format(channel))

@bot.command()
async def stoppls(ctx):
	'''Para de enviar mensagens'''
	if bot.bg_task:
		bot.bg_task.cancel()
		try:
			await bot.bg_task
		except asyncio.CancelledError:
			print('Task was sucessfully canceled')
		finally:
			pass
	await ctx.send('Ta bom, eu paro...')

@bot.event
async def background_task(channel,guild):
	await bot.wait_until_ready()
	while not bot.is_closed():
		current_time = datetime.datetime.now()
		current_hour = datetime.datetime.strftime(current_time,"%H:%M")
		current_day = datetime.datetime.strftime(current_time,"%a")
		next_day = datetime.datetime.strftime(current_time+datetime.timedelta(days=1),"%a")

		for hour in boss_schedule.keys():
			if current_hour < hour:
				next_boss_spawn = boss_schedule[hour][current_day]
				break
			# if there is no boss to spawn on the current day
			# then it should be the first boss of the next day
			next_boss_spawn = boss_schedule['02:00'][next_day]

		boss_names = []
		for boss in next_boss_spawn:
			boss_names.append((discord.utils.get(guild.roles, name=boss)))

		await print_next_boss_message(boss_names,hour,channel)

		await asyncio.sleep(60) # task runs every minute

bot.run(token)