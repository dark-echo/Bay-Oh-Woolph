from discord.ext import commands
from utils import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from member import Base, Member
import discord
import asyncio
from rank import Ranks



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
            
   @commands.command()
   @commands.has_role('Leadership')
   @asyncio.coroutine
   def addpoint(self, member1  : discord.Member=None):
       global session
       
       amember = member1
       
       storemember = []

       points = 0

       for member in session.query(Member).\
                 filter(Member.id ==  amember.id):
           storemember.append(member)
       
       if storemember:
           points = storemember[0].points

           points = points + 1

           session.query(Member).filter_by(id=amember.id).update({"points": points})
           session.commit()
           session.close()
       
           yield from self.bot.say("""You have gained a point {0}! Total points: """+str(points))

       else:
           yield from self.bot.say(""" No points for you imposter... """)








def setup(bot):
        bot.add_cog(Points(bot))


