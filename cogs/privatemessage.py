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
   @commands.has_any_role('The Dark Council','Leadership')
   async def rolemessage(self, ctx, mentionrole : discord.Role=None, *args):
       """Sends message to specified role via dm"""

       
       
       mod = self.bot.get_channel(int(MOD_LOG))

       await ctx.trigger_typing()

       for themember in self.bot.get_all_members():
           try:
               arole = [role for role in themember.roles if role.id == mentionrole.id] 
               if arole:
                   if arole[0].id == mentionrole.id: 
                       await themember.send( str(' '.join(args)))
                       await mod.send("Message successfully sent to: "+str(themember.name))
           except:
               await mod.send("Message failed to deliver: "+str(themember.name))
               continue

   @commands.command()
   @commands.has_any_role('The Dark Council','Leadership')
   async def sendmessage(self, ctx, member1  : discord.Member=None, *args):
       """Sends message to specified person via dm"""

       mod = self.bot.get_channel(int(MOD_LOG))

       await ctx.trigger_typing()

      
       try:
           await member1.send( str(' '.join(args)))
           await mod.send("Message successfully sent to: "+str(member1.name))
       except:
           await mod.send("Message failed to deliver: "+str(member1.name))
           

def setup(bot): 
    bot.add_cog(PrivateMessage(bot)) 


