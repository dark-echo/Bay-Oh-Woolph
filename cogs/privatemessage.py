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
   @asyncio.coroutine
   def sendmessage(self,*args): 
       """Sends message to all members via dm""" 

       memberrole = discord.Object(id=ROLE_MEMBER)
       
       mod = self.bot.get_channel(MOD_LOG) 

       yield from self.bot.type() 
   
       for themember in self.bot.get_all_members():
           try:
               arole = [role for role in themember.roles if role.id == memberrole.id] 
               if arole:
                   if arole[0].id == memberrole.id: 
                       yield from self.bot.send_message(themember, str(' '.join(args)))
                       yield from self.bot.send_message(mod, "Message successfully sent to: "+str(themember.name))
           except:
              yield from self.bot.send_message(mod, "Message failed to deliver: "+str(themember.name))           
              continue 

def setup(bot): 
    bot.add_cog(PrivateMessage(bot)) 


