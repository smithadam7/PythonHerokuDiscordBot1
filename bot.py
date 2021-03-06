# Python Discord Bot called Pyreply
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
import smtplib

client = commands.Bot(command_prefix=';')
player_dict = dict()


@client.event
async def on_ready():
    print("System Online")
    await client.change_presence(status=discord.Status.dnd) # set bot to do not distrub

@client.event
async def on_message(message):
    if message.author == client.user: # bot won't talk to itself
        return
    if message.content == "Hello":
        await client.send_message(message.channel, "Hello")

    searchObj = re.search( r'good game', message.content, re.M|re.I)
    if searchObj:
        await client.send_message(message.channel, "Good Game")

    skribblObj = re.search( r'skribbl.io', message.content, re.M|re.I)
    if skribblObj:
        await asyncio.sleep(5)
        await client.delete_message(message)

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

    monkeyObj = re.search( r'monkey', message.content, re.M|re.I)
    if monkeyObj:
        await client.add_reaction(message, "\U0001F412") # Python source code for emoji found at http://www.fileformat.info/info/unicode/char/search.htm

    burritoObj = re.search( r'burrito', message.content, re.M|re.I)
    if burritoObj:
        await client.add_reaction(message, "\U0001F32F") # Python source code for emoji found at http://www.fileformat.info/info/unicode/char/search.htm

    booObj = re.search( r'boo', message.content, re.M|re.I)
    if booObj:
        await client.add_reaction(message, "\U0001F47B") # Python source code for emoji found at http://www.fileformat.info/info/unicode/char/search.htm

    watermelonObj = re.search( r'watermelon', message.content, re.M|re.I)
    if watermelonObj:
        await client.add_reaction(message, "\U0001F349") # Python source code for emoji found at http://www.fileformat.info/info/unicode/char/search.htm

    await client.process_commands(message) # Allows client commands to work


@client.command(pass_context=True)
async def bye(ctx):
    server = ctx.message.server
    await client.send_message(ctx.message.channel, "bye")

@client.command(pass_context=True)
async def echoname(ctx):
    server = ctx.message.server
    await client.send_message(ctx.message.channel, ctx.message.author)

@client.command(pass_context=True)
async def edit(ctx):
    server = ctx.message.server
    await client.delete_message(ctx.message)
    await client.send_message(ctx.message.channel, "edited")

@client.command(pass_context=True)
async def status(ctx ,url):
    server = ctx.message.server
    req = requests.get(url)
    await client.send_message(ctx.message.channel, "Code: " + str(req.status_code)) # Use https://httpstat.us/ for different codes

#Send a custom text message via gmail to any number on the 4 main cell phone providers
@client.command(pass_context=True)
async def text(ctx, carrier, phonenumber, textmessage):
    server = ctx.message.server
    author = ctx.message.author
    await client.delete_message(ctx.message) #deletes message for privacy
    username = "prepaidburner@gmail.com"
    password = str(os.environ.get('EMAIL_PASS')) # set enviornment variable for the email password
    newcarrier = "default"
    sprintObj = re.search( r'sprint', carrier, re.M|re.I)
    if sprintObj:
        newcarrier = "@pm.sprint.com"
    verizonObj = re.search( r'verizon', carrier, re.M|re.I)
    if verizonObj:
        newcarrier = "@vtext.com"
    atObj = re.search( r'at', carrier, re.M|re.I)
    if atObj:
        newcarrier = "@mms.att.net"
    tmobileObj = re.search( r'tmo', carrier, re.M|re.I)
    if tmobileObj:
        newcarrier = "@tmomail.net"
    if newcarrier == "default":
        await client.send_message(ctx.message.channel, carrier + " carrier not supported.")
        return
    reciever = phonenumber + newcarrier
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(username, password)
    server.sendmail(username, reciever, textmessage)
    server.quit()
    await client.send_message(ctx.message.channel, "A private user" + " has sent a private message to a private number.")

@client.command(pass_context=True)
async def add(ctx, left: int, right: int):
    server = ctx.message.server
    await client.send_message(ctx.message.channel, left + right)

@client.command(pass_context=True)
async def mul(ctx, left: int, right: int):
    server = ctx.message.server
    await client.send_message(ctx.message.channel, left * right)

@client.command(pass_context=True)
async def pow(ctx, left: int, right: int):
    server = ctx.message.server
    await client.send_message(ctx.message.channel, left ** right)

@client.command(pass_context=True)
async def sub(ctx, left: int, right: int):
    server = ctx.message.server
    await client.send_message(ctx.message.channel, left - right)

@client.command(pass_context=True)
async def div(ctx, left: int, right: int):
    server = ctx.message.server
    await client.send_message(ctx.message.channel, left / right)

@client.command(pass_context=True)
async def mod(ctx, left: int, right: int):
    server = ctx.message.server
    await client.send_message(ctx.message.channel, left % right)

@client.command(pass_context=True)
async def helpme(ctx): # help is predefined
    server = ctx.message.server
    await client.send_message(ctx.message.channel, "https://github.com/smithadam7/PythonHerokuDiscordBot1/blob/master/README.md")

@client.command(pass_context=True)
async def relinquish(ctx):
    server = ctx.message.server
    x = ctx.message.server.members
    namelist = []
    for member in x:
        namelist.append(member.name)
    await client.send_message(ctx.message.channel, "Relinquish Successful! " + str(random.choice(namelist)) + " is now yeetmaster.")


client.run(str(os.environ.get('BOT_TOKEN'))) # enviornment variable for the bot token