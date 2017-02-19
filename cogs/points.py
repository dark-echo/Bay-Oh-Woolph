from discord.ext import commands
from utils import *
import discord
import asyncio

from member import Member
class Points:

    def __init__(self,bot):
        self.bot = bot

#Test method to populate an array from discord -Infinite
    @bot.command()
    @asyncio.coroutine
    def getmembers(self):
    #Intialize array
        listOfMembers = [] 

        #Add members to array
        for member in self.bot.get_all_members():
            listOfMembers.append(Member(parseStr(member.id),member.name,member.nick,member.top_role,0))

        #Fetch the a member at [x] index added to the array.
        sentence = listOfMembers[8].displayMember()
        #Get length of array.
        length = len(listOfMembers)

        yield from self.bot.say(str(sentence))
        yield from self.bot.say("NumberofMembersinArray: "+str(length))

def setup(bot):
    bot.add_cog(Points(bot))


