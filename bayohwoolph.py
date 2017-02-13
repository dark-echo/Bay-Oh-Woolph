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

#Parse a string to primitive type based on content using lambda expression 
import string
parseStr = lambda x: x.isalpha() and x or x.isdigit() and \
                int(x) or x.isalnum() and x or \
                len(set(string.punctuation).intersection(x)) == 1 and \
                x.count('.') == 1 and float(x) or x


initial_extensions = [
    'cogs.basicpromotions',
]

logging.basicConfig(level=logging.DEBUG)

config = configparser.ConfigParser()
for inifile in [os.path.expanduser('~')+'/.bayohwoolph.ini','bayohwoolph.local.ini','bayohwoolph.ini']:
    if os.path.isfile(inifile):
        config.read(inifile)
        break # First config file wins
MAIN = config['MAIN']

description = '''Dark Echo's barkeep'''

bot = commands.Bot(command_prefix=commands.when_mentioned_or(MAIN.get('commandchar')), description=description)


@bot.event
@asyncio.coroutine
def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    

@bot.command()
@asyncio.coroutine
#Test method to populate an array from discord -Infinite
def getmembers():
    #Intialize array
    listOfMembers = [] 

    #Add members to array
    for member in bot.get_all_members():
        listOfMembers.append(Member(parseStr(member.id),member.name,member.nick,member.top_role,0))

    #Fetch the a member at [x] index added to the array.
    sentence = listOfMembers[8].displayMember()
    #Get length of array.
    length = len(listOfMembers)

    yield from bot.say(str(sentence))
    yield from bot.say("NumberofMembersinArray: "+str(length))


# Everything should go above this
if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print('Failed to load extension {}\n{}: {}'.format(extension, type(e).__name__, e))
    bot.run(MAIN.get('login_token'))
## Nothing goes after this comment! ##
