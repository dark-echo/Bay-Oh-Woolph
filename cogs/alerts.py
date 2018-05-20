from discord.ext import commands
from utils import *
import discord
import asyncio
from config import Config

import logging
logger = logging.getLogger('bayohwoolph.cogs.alerts')

ALERTS = Config.config['ALERTS']

HIGH_COMMAND = ALERTS['high_command']
WELCOME_ROOM = ALERTS['welcome_room']
LEAVE_NOTICE_ROOM = ALERTS['MOD_LOG']

class Alerts:
    """Automatic notifications about stuff."""
    
    def __init__(self, bot):
        self.bot = bot

    @asyncio.coroutine
    def on_member_join(self, member):
        welcomeroom = self.bot.get_channel(WELCOME_ROOM)
        yield from self.bot.send_message(welcomeroom,"Salutations {0.mention}! Welcome to Dark Echo's Discord server. Please speak up and a <@&174254896260972544> or <@&146724062301913088> will help you shortly.".format(member))

    @asyncio.coroutine
    def on_member_remove(self, member):
        alertroom = self.bot.get_channel(LEAVE_NOTICE_ROOM)
        msg = '<{0.mention} left.'

        yield from self.bot.send_message(alertroom,msg.format(member))
        
def setup(bot):
    bot.add_cog(Alerts(bot))
