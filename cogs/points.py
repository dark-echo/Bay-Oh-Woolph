from discord.ext import commands
from utils import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from member import Base, Member
from rank import Ranks
from utility.dbproc import Baydb
import discord
import asyncio




class Points:
   
   engine = create_engine('sqlite:///bayohwoolph.db')
   Base.metadata.bind = engine
   DBSession = sessionmaker(bind=engine)
   global session
   session = DBSession()

   def __init__(self,bot):
        self.bot = bot

#Test method to populate an array from discord -Infinite
   @commands.command()
   @commands.has_role('Leadership')
   @asyncio.coroutine
   def updateroster(self, role1 : discord.Role=None):
        """Update roster for Dark Echo based on role."""
        
        global session
       
        
        therole = role1
    #Typing function
        yield from self.bot.type()
    #Intialize array
        listOfMembers = [] 

        #Add members to array
        for themember in self.bot.get_all_members():
            arole = [role for role in themember.roles if role == therole]
            if arole:
                if arole[0].name == therole.name:
                    listOfMembers.append(Member(int(themember.id),str(themember.name),str(themember.nick),str(themember.top_role)))
        
          
        for amember in listOfMembers:
            session.merge(amember)

        session.commit()
        session.close()        
        

        yield from self.bot.say("DB successfully updated")
    
   #Add points command        
   @commands.command()
   @commands.has_role('Leadership')
   @asyncio.coroutine
   def addpoint(self, member1  : discord.Member=None, pv=None):
       
       

       amember = member1
       storemember = []

       points = 0

       try:
           pointvalue = int(pv)
           Baydb.updatepoints(amember,storemember,points,pointvalue)
       
           yield from self.bot.say("command ran fully");
       except:
           yield from self.bot.say("Invalid point value");


def setup(bot):
        bot.add_cog(Points(bot))


