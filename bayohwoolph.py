#!/usr/bin/python3
import asyncio
import configparser
import discord
import os
from discord.ext import commands

# Parse the config and stick in global "config" var
config = configparser.ConfigParser()
for inifile in [os.path.expanduser('~')+'/.bayohwoolph.ini','bayohwoolph.local.ini','bayohwoolph.ini']:
    if os.path.isfile(inifile):
        config.read(inifile)
        break # First config file wins
MAIN = config['MAIN']

description = '''Dark Echo's barkeep'''
bot = commands.Bot(command_prefix='$', description=description)

@bot.event
@asyncio.coroutine
def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

bot.run(MAIN.get('login_token'))
