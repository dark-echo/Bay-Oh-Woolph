from discord.ext import commands
from utils import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from member import Base, Member
import discord
import asyncio
from rank import Ranks



class Baydb:
   
   engine = create_engine('sqlite:///C:\\Users\\Daniel\\Source\Repos\\Bay-Oh-Woolph\\bayohwoolh.db')
   Base.metadata.bind = engine
   DBSession = sessionmaker(bind=engine)
   global session
   session = DBSession()

   def __init__(self, bot):
        self.bot = bot
    
   @asyncio.coroutine
   def pointinsert(amember,storemember,points,pointvalue):  
           global session
           
           if pointvalue.is_integer():
               
               for member in session.query(Member).\
                         filter(Member.id ==  amember.id):
                   storemember.append(member)
       
               if storemember:
                   points = storemember[0].points

                   points = points + pointvalue

                   session.query(Member).filter_by(id=amember.id).update({"points": points})
                   session.commit()
                   session.close()
       
                   yield from self.bot.say("You have gained "+pointvalue+" point(s) {0.mention}!".format(amember)+" Total points: "+str(points))

               else:
                   yield from self.bot.say(" No points for you imposter... ")
           else:
                yield from self.bot.say("Invalid point value,")
                

            







def setup(bot):
        bot.add_cog(Baydb(bot))


