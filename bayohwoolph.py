#!/usr/bin/python3
# General libraries
import asyncio
import discord
import os
import logging

from config import Config

from discord.ext import commands

# Our specific stuff
from utils import *


initial_extensions = [
    'cogs.basicpromotions',
    'cogs.alerts',
    'cogs.points',
    'cogs.updateroster'
]

MAIN = Config.MAIN

# pull debug level from config
debug = Config.debug

# Create global logger object
logger = logging.getLogger('bayohwoolph')
    
description = '''Dark Echo's barkeep'''

bot = commands.Bot(command_prefix=commands.when_mentioned_or(MAIN.get('commandchar'), '<@&277976387543891968> '), description=description)

@bot.event
@asyncio.coroutine
def on_ready():
    logger.info('Logged in as %r (%r)' % (bot.user.name, bot.user.id))

# Everything should go above this
if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            logger.debug('Trying to load extension: ' + extension)
            bot.load_extension(extension)
        except Exception as e:
            logger.error('Failed to load extension {}\n{}: {}'.format(extension, type(e).__name__, e))
    bot.run(MAIN.get('login_token'))
## Nothing goes after this comment! ##
