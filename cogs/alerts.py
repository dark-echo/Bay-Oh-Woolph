from discord.ext import commands
from utils import *
import discord
import asyncio
from config import Config

import logging
logger = logging.getLogger('bayohwoolph.cogs.alerts')

ALERTS = Config.config['ALERTS']

HIGH_COMMAND = ALERTS['high_command']
LOBBY = ALERTS['lobby']
BOT_DEV = ALERTS['bot_dev']

class Alerts:
    """Automatic notifications about stuff."""
    
    def __init__(self, bot):
        self.bot = bot

    @asyncio.coroutine
    def on_member_join(self, member):
        botdev = self.bot.get_channel(BOT_DEV)
        yield from self.bot.send_message(botdev,"Salutations {0.mention}! Welcome to Dark Echo's Discord server. Please speak up and <@&146724062301913088> will get your roles sorted shortly.".format(member))

    @asyncio.coroutine
    def on_member_remove(self, member):
        botdev = self.bot.get_channel(BOT_DEV)
        msg = '<@&146724062301913088> {0.mention} left.'

        yield from self.bot.send_message(botdev,msg.format(member))
        
def setup(bot):
    bot.add_cog(Alerts(bot))
