#!/usr/bin/python3
# General libraries
import asyncio
import configparser
import discord
import os
import logging
from discord.ext import commands

# Our specific stuff
from utils import *


initial_extensions = [
    'cogs.basicpromotions',
    'cogs.alerts',
    'cogs.points',
]

# logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.INFO)

config = configparser.ConfigParser()
for inifile in [os.path.expanduser('~')+'/.bayohwoolph.ini','bayohwoolph.local.ini','bayohwoolph.ini']:
    if os.path.isfile(inifile):
        config.read(inifile)
        break # First config file wins
MAIN = config['MAIN']

description = '''Dark Echo's barkeep'''

bot = commands.Bot(command_prefix=commands.when_mentioned_or(MAIN.get('commandchar'), '<@&280045122614198292> '), description=description)

@bot.event
@asyncio.coroutine
def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

    discord.Message.content.
@bot.event
async def on_message(message):
        if message.content.con:
            await client.send_message(message.channel, 'Say hello')
            msg = await client.wait_for_message(author=message.author, content='hello')
            await client.send_message(message.channel, 'Hello.')

# Everything should go above this
if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print('Failed to load extension {}\n{}: {}'.format(extension, type(e).__name__, e))
    bot.run(MAIN.get('login_token'))
## Nothing goes after this comment! ##
