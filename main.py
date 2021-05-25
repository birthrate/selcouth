import discord
import os
from discord.ext import commands

TOKEN = 'ODI2Mjc3NjYyODQ1ODI5MTIw.YGKJCg.xnJiCgP62fMKdYJXvTcoEe75B7Y'

intents = discord.Intents().all()
client = commands.Bot(command_prefix = '.', intents = intents)
client.remove_command('help')

@client.command()
@commands.has_role('developer')
async def load(ctx, extension):
    embed = discord.Embed(
        title = '',
        description = 'Loaded Successfully',
        colour=0x008000
    )

    embed.set_footer(text='main.py')
    client.load_extension(f'cogs.{extension}')
    await ctx.send(embed=embed)

@client.command()
@commands.has_role('developer')
async def unload(ctx, extension):
    embed = discord.Embed(
        title = '',
        description = 'Unloaded Successfully',
        colour=0x008000
    )

    embed.set_footer(text='main.py')
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(embed=embed)

@client.command()
@commands.has_role('developer')
async def reload(ctx, extension):
    embed = discord.Embed(
        title = '',
        description = 'Reloaded Successfully',
        colour=0x008000
    )

    embed.set_footer(text='main.py')
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send(embed=embed)


# @commands.command()
# @commands.is_owner()
# async def restart(self, ctx):
#     await ctx.bot.logout()
#     await ctx.bot.login("ODI2Mjc3NjYyODQ1ODI5MTIw.YGKJCg.xnJiCgP62fMKdYJXvTcoEe75B7Y", bot=True)
#     embed = discord.Embed(
#     title = '',
#     description = 'Restarted Successfully',
#     colour=0x008000
#     )

#     embed.set_footer(text='Selcouth Development')

#     await ctx.send(embed=embed)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(TOKEN)

# TODO: tickets
# * fix .selcouth // priority=low
# temp mute
