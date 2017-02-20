from discord.ext import commands
from utils import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from member import Base, Member
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
   def getmembers(self, role1 : discord.Role=None):
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
                    listOfMembers.append(Member(int(themember.id),str(themember.name),str(themember.nick),str(themember.top_role),0))
        
          
        for amember in listOfMembers:
            session.add(amember)

        session.commit()
                
        length = len(listOfMembers)

        yield from self.bot.say("Number of " + str(therole) + "s in array: " + str(length))
            
     
       


        

def setup(bot):
    bot.add_cog(Points(bot))


