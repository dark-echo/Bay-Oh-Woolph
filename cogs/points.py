from discord.ext import commands
from utils import *
import discord
import asyncio
import sqlite3


from member import Member
class Points:
   
   

   def __init__(self,bot):
        self.bot = bot

#Test method to populate an array from discord -Infinite
   @commands.command()
   @commands.has_role('Leadership')
   @asyncio.coroutine
   def getmembers(self, role1 : discord.Role=None):
        
       
        
        therole = role1
    #Typing function
        yield from self.bot.type()
    #Intialize array
        listOfMembers = [] 

        #Add members to array
        for amember in self.bot.get_all_members():
            arole = [role for role in amember.roles if role == therole]
            if arole:
                if arole[0].name == therole.name:
                    listOfMembers.append(Member(int(amember.id),str(amember.name),str(amember.nick),str(amember.top_role),0))
                
        length = len(listOfMembers)

        yield from self.bot.say("Number of " + str(therole) + "s in array: " + str(length))
            
     
       


        

def setup(bot):
    bot.add_cog(Points(bot))


