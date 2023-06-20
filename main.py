# TOKEN = 'bcfcf78d1eca4e735a8a7672b765b760bacefdaa8df735b2b090c0b8c5284a83'

import discord

TOKEN = 'bcfcf78d1eca4e735a8a7672b765b760bacefdaa8df735b2b090c0b8c5284a83'

client = discord.Client()


@client.command(pass_context=True)
async def chnick(ctx, member: discord.Member, nick):
    await member.edit(nick=nick)
    await ctx.send(f'Nickname was changed for {member.mention} ')


async def on_ready():
    print('ログインしました')


client.run(TOKEN)
