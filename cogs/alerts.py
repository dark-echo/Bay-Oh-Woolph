from discord.ext import commands
from utils import *
import discord
import asyncio

HIGH_COMMAND = '146729963012227073'
LOBBY = '146723400671428608'

class Alerts:
    """Automatic notifications about stuff."""
    
    def __init__(self, bot):
        self.bot = bot

    @asyncio.coroutine
    def on_member_join(self, member):
        lobby = self.bot.get_channel(LOBBY)
        yield from self.bot.send_message(lobby,"Salutations {0.mention}! Welcome to Dark Echo's Discord server. Please speak up and <@&146724062301913088> will get your roles sorted shortly.".format(member))

    @asyncio.coroutine
    def on_member_remove(self, member):
        highcommand = self.bot.get_channel(HIGH_COMMAND)
        msg = '<@&146724062301913088> {0.mention} left.'

        yield from self.bot.send_message(highcommand,msg.format(member))
        
def setup(bot):
    bot.add_cog(Alerts(bot))
