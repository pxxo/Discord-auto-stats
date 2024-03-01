import discord
from discord.ext import commands
# TOKEN = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    await ctx.send(f'Hello, {ctx.author.name}!')


@bot.command()
async def hello(ctx):
    await ctx.send(f'Hello, {ctx.author.name}!')

bot.run(TOKEN)
