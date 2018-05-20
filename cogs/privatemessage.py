from discord.ext import commands 
from utils import * 
from bayohwoolph import bot 
import discord 
import asyncio 
import logging 

logger = logging.getLogger('bayohwoolph.cogs.privatemessage')

from config import Config 

UPDATEROSTER = Config.config['UPDATEROSTER']

ROLE_MEMBER = UPDATEROSTER['ROLE_MEMBER']

MOD_LOG = UPDATEROSTER['MOD_LOG']

class PrivateMessage: 

   def __init__(self,bot):
       self.bot = bot 

   @commands.command()
   @commands.has_any_role('Admin')
   async def sendmessage(self, ctx, *args):
       """Sends message to all members via dm"""

       memberrole = discord.utils.get(ctx.guild.roles, id=int(ROLE_MEMBER))
       
       mod = self.bot.get_channel(int(MOD_LOG))

       await ctx.trigger_typing()

       for themember in self.bot.get_all_members():
           try:
               arole = [role for role in themember.roles if role.id == memberrole.id] 
               if arole:
                   if arole[0].id == memberrole.id: 
                       await themember.send( str(' '.join(args)))
                       await mod.send("Message successfully sent to: "+str(themember.name))
           except:
               await mod.send("Message failed to deliver: "+str(themember.name))
               continue

def setup(bot): 
    bot.add_cog(PrivateMessage(bot)) 


