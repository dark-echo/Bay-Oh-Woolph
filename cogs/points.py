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




class Points:
   
   
    def __init__(self,bot):
        self.bot = bot

    global session

    session = Baydb.session

    global ROLE_MEMBER

    ROLE_MEMBER = '284029774513569793'

    global conn
    conn = Baydb.conn


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

    # Event Checkin
    @commands.command(pass_context=True)
    @asyncio.coroutine
    def checkin(self,ctx):
        """Adds points to specified member."""

        amember = ctx.message.author
        storemember = []
        points = 0
        #date








        for member in session.query(Member). \
                filter(Member.id == amember.id):
            storemember.append(member)

        if storemember:
            points = storemember[0].points

            points = points + 1

            current_time = _datetime.datetime.utcnow()

            dateparams = [null, current_time + _datetime.timedelta(weeks=1)]

            checkdate = select([Member.checkInDate], Member.checkInDate.in_(dateparams))

            result = conn.execute(checkdate)

            if checkdate == dateparams[0] or checkdate == dateparams[1]:
                yield from self.bot.type()

                session.query(Member).filter_by(id=amember.id).update({"points": points})
                session.commit()
                session.close()

                yield from self.bot.say(
                    "You have gained a checkin point {0.mention}!".format(
                        amember) + " Total points: " + str(
                        points))

        else:
            yield from self.bot.say(" No points for you imposter... ")









def setup(bot):
        bot.add_cog(Points(bot))


