from discord.ext import commands
from utils import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import *
from member import Base, Member
from utility.dbproc import Baydb
import _datetime
import discord
import asyncio

from config import Config

import logging
logger = logging.getLogger('bayohwoolph.cogs.utility')




class Utility:   
    """Utility Functions"""

    def __init__(self,bot):
        self.bot = bot



    #Add points command
    @commands.command()
    @asyncio.coroutine
    def gametime(self,ctx):
        '''Displays gametime in Elite Dangerous'''
        




        milutcnow = _datetime.datetime.utcnow().strftime("%H:%M:%S")

        yield from self.bot("Time in Elite Dangerous(*Military Time*): **"+milutcnow+"**")
 
        
        

def setup(bot):
        bot.add_cog(Utility(bot))


