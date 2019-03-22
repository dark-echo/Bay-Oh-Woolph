#!/usr/bin/python3.6
# General libraries
import asyncio
import discord
import os
import logging

from config import Config

from discord.ext import commands

# Our specific stuff
from utils import *

# "Cog" extensions loaded a little later
initial_extensions = [
    'cogs.basicpromotions',
    'cogs.alerts',
    'cogs.points',
    'cogs.updateroster',
    'cogs.privatemessage',
    'cogs.memberinfo',
    'cogs.utility',
    'cogs.mgmanager',
    'cogs.games'
]

MAIN = Config.MAIN

# pull debug level from Config class
debug = Config.debug

# Create global logger object
logger = logging.getLogger('bayohwoolph')
    
description = '''Dark Echo's barkeep'''

bot = commands.Bot(command_prefix=commands.when_mentioned_or(MAIN.get('commandchar'), '<@&277976387543891968> '), description=description)

@bot.event
async def on_ready():
    logger.info('Logged in as %r (%r)' % (bot.user.name, bot.user.id))
    await bot.change_presence(activity=discord.Game(name="Serving Drinks for DE"))

# Everything should go above this
if __name__ == '__main__':

    # Loop through extensions and load them:
    for extension in initial_extensions:
        try:
            logger.debug('Trying to load extension: ' + extension)
            bot.load_extension(extension)
        except Exception as e:
            logger.error('Failed to load extension {}\n{}: {}'.format(extension, type(e).__name__, e))

    # Start the main execution loop up:
    bot.run(MAIN.get('login_token'))
    bot.close()
## Nothing goes after this comment! ##
