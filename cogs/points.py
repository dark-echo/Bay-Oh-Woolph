from discord.ext import commands
from utils import *
import discord
import asyncio


class Points:
    
    from member import Member
    #Parse a string to primitave type based on content using lambda expression 
    import string
    parseStr = lambda x: x.isalpha() and x or x.isdigit() and \
                int(x) or x.isalnum() and x or \
                len(set(string.punctuation).intersection(x)) == 1 and \
                x.count('.') == 1 and float(x) or x

    def __init__(self,bot):
        self.bot = bot

#Test method to populate an array from discord -Infinite
    @commands.command()
    @commands.has_role('Leadership')
    @asyncio.coroutine
    def getmembers(self):
    #Intialize array
        listOfMembers = [] 

        #Add members to array
        for member in self.bot.get_all_members():
            listOfMembers.append(Member(parseStr(member.id),member.name,member.nick,member.top_role,0))

        
        #Get length of array.
        length = len(listOfMembers)


        yield from self.bot.say("NumberofMembersinArray: " + str(length))

def setup(bot):
    bot.add_cog(Points(bot))


