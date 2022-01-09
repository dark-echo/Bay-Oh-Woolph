from discord.ext import commands
from utils import *
from bayohwoolph import bot
import discord
import asyncio

from config import Config

import logging
logger = logging.getLogger('bayohwoolph.cogs.rolegranttemp')

UPDATEROSTER = Config.config['UPDATEROSTER']

MOD_LOG = UPDATEROSTER['MOD_LOG']

class RoleGrantTemp(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def grantrole(self,ctx,member : discord.Member=None,roletogrant : discord.Role=None):

        mod = self.bot.get_channel(int(MOD_LOG))
    
        

        try:
            await member.add_roles(roletogrant)
            await mod.send("Role of: "+str(roletogrant.name)+" successfully granted to: "+str(member.name))
        except:
            await mod.send("Failed to add role to user")
         
        
def setup(bot):
    bot.add_cog(RoleGrantTemp(bot))



