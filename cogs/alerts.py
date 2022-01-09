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





class Alerts(commands.Cog):
    """Automatic notifications about stuff."""
    
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self,member):
        welcomeroom = self.bot.get_channel(int(WELCOME_ROOM))
        await asyncio.sleep(5)
        await welcomeroom.send("Salutations {0.mention}! Welcome to Dark Echo's Discord server. Please speak up and a <@&174254896260972544> or <@&146724062301913088> will help you shortly. If you are here for multigame or games other than elite dangerous, please use $multigame to get started.".format(member))

    @commands.Cog.listener()
    async def on_member_remove(self,member):
        alertroom = self.bot.get_channel(int(LEAVE_NOTICE_ROOM))
        msg = '<{0.mention} left.'

        await alertroom.send(msg.format(member))
        
def setup(bot):
    bot.add_cog(Alerts(bot))
