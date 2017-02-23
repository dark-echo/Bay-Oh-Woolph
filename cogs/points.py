from discord.ext import commands
from utils import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import exists
from member import Base, Member
from utility.dbproc import Baydb
import discord
import asyncio




class Points:
   
   
    def __init__(self,bot):
        self.bot = bot

    global session

    session = Baydb.session

    global ROLE_MEMBER

    ROLE_MEMBER = '284029774513569793'



    #Add points command
    @commands.command()
    @commands.has_role('Leadership')
    @asyncio.coroutine
    def addpoint(self, member1  : discord.Member=None, pv=None):
        """Adds points to specified member."""

        amember = member1
        storemember = []
        points = 0

        try:
            pointvalue = int(pv)
        except (ValueError, TypeError):
            yield from self.bot.say("Invalid Point Value")




        if  pointvalue:

            yield from self.bot.type()

            for member in session.query(Member). \
                    filter(Member.id == amember.id):
                storemember.append(member)

            if storemember:
                points = storemember[0].points

                points = points + pointvalue

                session.query(Member).filter_by(id=amember.id).update({"points": points})
                session.commit()
                session.close()

                yield from self.bot.say(
                    "You have gained " + str(pointvalue) + " point(s) {0.mention}!".format(amember) + " Total points: " + str(
                        points))

            else:
                yield from self.bot.say(" No points for you imposter... ")

                # Add points command







def setup(bot):
        bot.add_cog(Points(bot))


