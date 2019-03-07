# Python Discord Bot
# Add to server with this https://discordapp.com/oauth2/authorize?client_id=CLIENTID&scope=bot CLIENTID is found under OAuth2 in discord developer portal
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random
import requests
import os # For use of environ, which is for heroku to use environment var bot token
import re # For use of regex
from discord import opus

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
async def bye(ctx):
    server = ctx.message.server
    await client.send_message(ctx.message.channel, "bye")

@client.command(pass_context=True)
async def downstatus(ctx ,url):
    server = ctx.message.server
    req = requests.get(url)
    await client.send_message(ctx.message.channel, req.status_code)

@client.command(pass_context=True)
async def add(ctx, left: int, right: int):
    server = ctx.message.server
    await client.send_message(ctx.message.channel, left + right)


client.run(str(os.environ.get('BOT_TOKEN')))