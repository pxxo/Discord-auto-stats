# TOKEN = 'MTEyMDQwOTg3Njg1MDU1Njk4OA.GMBzX5.URv4gkARf6J2pDasb60Hzhn1lQxjNgp21rtRKc'
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    await ctx.send(f'Hello, {ctx.author.name}!')


@bot.command()
async def hello(ctx):
    await ctx.send(f'Hello, {ctx.author.name}!')

bot.run('MTEyMDQwOTg3Njg1MDU1Njk4OA.GMBzX5.URv4gkARf6J2pDasb60Hzhn1lQxjNgp21rtRKc')
