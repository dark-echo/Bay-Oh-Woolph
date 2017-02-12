#!/usr/bin/python3
# General libraries
import asyncio
import configparser
import discord
import os
import logging
from discord.ext import commands

# Our specific stuff
import utils

logging.basicConfig(level=logging.DEBUG)

global config
# Parse the config and stick in global "config" var
config = configparser.ConfigParser()
for inifile in [os.path.expanduser('~')+'/.bayohwoolph.ini','bayohwoolph.local.ini','bayohwoolph.ini']:
    if os.path.isfile(inifile):
        config.read(inifile)
        break # First config file wins
global MAIN
MAIN = config['MAIN']


description = '''Dark Echo's barkeep'''
global bot
bot = commands.Bot(command_prefix=commands.when_mentioned_or('$'), description=description)


@bot.event
@asyncio.coroutine
def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

newcadetmsg = """
Welcome to Dark Echo, {0.mention}!

:echoBlue: Here are the basic steps to get started with Dark Echo: :echoBlue: 

1. Sign up for a forum account at http://darkecho.org/forums/ucp.php?mode=register
2. If you use Inara, join us at http://inara.cz/wing/300
3. In the game, under "Friends and Private Groups", request membership in the "Dark Echo" private group and send "Dark Echo" a friend request.
4. Send in-game friend requests to the Echoes you see currently active on Discord and/or via in the in-game private group.
5. Move your primary base of operations (any additional ships, etc) to Snodgrass Orbital in Disci.
6. Once your forum account is activated, look for "Getting Started" instructions there.

Note: You cannot get to Disci in a starter sidewinder. You need a ship with at least a 9.5LY jump range. If you can't plot a route directly, try plotting a route to Wolf 412 and then plotting a route from there. If you can upgrade most components from "E" to "D" rated in a Sidewinder or Eagle, you should be able to make it. Or a stock Hauler can make it. If you're still having trouble, talk to us on Discord and I'm sure somebody will be willing to help you out.

Make sure you get that forum account set up, since that's what we use to track how long you've been a Cadet.

Please set an avatar image in Discord, as it greatly helps with telling people apart when using the in-game overlay.

If you stay active with us for a couple of weeks and haven't heard about a promotion to Officer, please remind the @Leadership.
"""

@bot.command()
@commands.has_role('Leadership')
@asyncio.coroutine
def newcadet(member : discord.Member):
    """Give intro message to new cadet and assign them cadet role."""
    global bot

    yield from bot.type()

    cadetrole = discord.Object(id=146725461727117314)
    yield from bot.add_roles(member,cadetrole)

    yield from bot.say(newcadetmsg.format(member))

    
bot.run(MAIN.get('login_token'))
