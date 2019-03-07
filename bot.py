import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random
import requests
import os
import re

client = commands.Bot(command_prefix=';')
player_dict = dict()


@client.event
async def on_ready():
    print("System Online")

@client.event
async def on_message(message):
    if message.author == client.user: # bot won't talk to itself
        return
    if message.content == "Hello":
        await client.send_message(message.channel, "Hello")

    searchObj = re.search( r'gg', message.content, re.M|re.I)
    if searchObj:
        await client.send_message(message.channel, "GG")

    flipObj = re.search( r'flip', message.content, re.M|re.I)
    if flipObj:
        htseq = ["Heads","Tails"] # Head or Tails Sequence for flipping a coin
        await client.send_message(message.channel, random.choice(htseq))

    fireObj = re.search( r'fire', message.content, re.M|re.I)
    if fireObj:
        await client.add_reaction(message, "\U0001F525") # Python source code for emoji found at http://www.fileformat.info/info/unicode/char/search.htm

    pooObj = re.search( r'poo', message.content, re.M|re.I)
    if pooObj:
        await client.add_reaction(message, "\U0001F4A9") # Python source code for emoji found at http://www.fileformat.info/info/unicode/char/search.htm

    await client.process_commands(message) # Allows client commands to work

@client.command(pass_context=True)
async def play(ctx, url):
    channel = ctx.message.author.voice_channel
    await client.join_voice_channel(channel)
    server = ctx.message.server
    voice = client.voice_client_in(server)
    player = await voice.create_ytdl_player(url)
    player_dict[server.id] = player
    await client.send_message(ctx.message.channel, "Playing `%s` now" % player.title)
    player.start()


@client.command(pass_context=True)
async def stop(ctx):
    server = ctx.message.server
    player = player_dict[server.id]
    player.stop()
    await client.send_message(ctx.message.channel, "Stopped `%s`" % player.title)
    del player_dict[server.id]


@client.command(pass_context=True)
async def pause(ctx):
    server = ctx.message.server
    player = player_dict[server.id]
    player.pause()
    await client.send_message(ctx.message.channel, "Paused `%s`" % player.title)


@client.command(pass_context=True)
async def resume(ctx):
    server = ctx.message.server
    player = player_dict[server.id]
    player.resume()
    await client.send_message(ctx.message.channel, "Resumed `%s`" % player.title)

@client.command(pass_context=True)
async def bye(ctx):
    server = ctx.message.server
    await client.send_message(ctx.message.channel, "bye")

@client.command(pass_context=True)
async def leave(ctx):
    client.close()

@client.command(pass_context=True)
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)


client.run(str(os.environ.get('BOT_TOKEN')))