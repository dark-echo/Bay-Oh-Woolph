from discord.ext import commands
from utils import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import *
from member import Base, Member, Rank
from utility.dbproc import Baydb
from bayohwoolph import bot
import discord
import asyncio
import logging

import logging
logger = logging.getLogger('bayohwoolph.cogs.updateroster')


from config import Config

UPDATEROSTER = Config.config['UPDATEROSTER']

ROLE_MEMBER = UPDATEROSTER['ROLE_MEMBER']
MOD_LOG = UPDATEROSTER['MOD_LOG']

session = Baydb.session
conn = Baydb.conn


#Command to Update Roster
class MemberInfo:
    """Admin tools for updating bot's internal roster info."""

    def __init__(self, bot):
        self.bot = bot
    #assign bot to bayohwoolpbot
    
    session = Baydb.session 
    conn = Baydb.conn 
    
     

    @commands.command()
    @commands.has_role('Leadership')
    @asyncio.coroutine
    def whois(self,ctx):
        """Search for a member."""

        memattribute = ctx 

        query = session.query(Member).filter(or_(Member.id.like(memattribute),Member.globalName.like(memattribute),Member.nickname.like(memattribute)))
        for themember in query:
          #Will be fixed.
           member = str(themember.name)
           yield from self.bot.say("Member Info: " + str(member)) 



def setup(bot):
    bot.add_cog(MemberInfo(bot))
