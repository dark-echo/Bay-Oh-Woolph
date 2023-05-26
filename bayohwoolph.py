#!/usr/bin/python3.9.6
# General libraries
import asyncio
import discord
import aiohttp
import os
import logging
from config import Config
from discord.ext import commands,tasks

#Utils import
from utils import * 


MAIN = Config.MAIN

# pull debug level from Config class
debug = Config.debug

#Create global logger object
logger = logging.getLogger('bayohwoolph')

description = '''Dark Echo's barkeep'''

intents = discord.Intents.all()
intents.members = True
#Put debugging code back async style for errors.
class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=commands.when_mentioned_or(MAIN.get('commandchar'), '<@&277976387543891968> '), description=description, intents=intents)
        self.initial_extensions = [
              'cogs.basicpromotions',
              'cogs.alerts',
              'cogs.points',
              'cogs.updateroster',
              'cogs.privatemessage',
              'cogs.utility',
              'cogs.mgmanager',
              'cogs.games'
           ]

    async def setup_hook(self):
        for ext in self.initial_extensions:
            await self.load_extension(ext)

    async def close(self):
        await super().close()

    async def on_ready(self):
        await bot.change_presence(activity=discord.Game(name="Serving Drinks for DE"))
        print('Ready!')

bot = MyBot()
bot.run(MAIN.get('login_token'))

