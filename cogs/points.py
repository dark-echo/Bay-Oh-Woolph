from discord.ext import commands
from utils import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import *
from member import Base, Member
from utilities.dbproc import Baydb
import _datetime
import discord
import asyncio

from config import Config

import logging
logger = logging.getLogger('bayohwoolph.cogs.points')

POINTS = Config.config['POINTS']


class Points:   
    """Tools for tracking rank-related 'points' for Dark Echo Members."""

    def __init__(self,bot):
        self.bot = bot

    global session

    session = Baydb.session

    global ROLE_MEMBER

    ROLE_MEMBER = POINTS['ROLE_MEMBER']

    global conn
    conn = Baydb.conn


    #Add points command
    @commands.command()
    @commands.has_role('Leadership')
    async def addpoints(self, ctx, member1  : discord.Member=None, pv=None):
        """Add points to specified member."""

        amember = member1
        storemember = []
        points = 0

        try:
            pointvalue = int(pv)
        except (ValueError, TypeError):
            await ctx.send("Invalid Point Value")

        if  pointvalue:

            await ctx.trigger_typing()

            for member in session.query(Member). \
                    filter(Member.id == amember.id):
                storemember.append(member)

            if storemember:
                points = storemember[0].points

                points = points + pointvalue

                session.query(Member).filter_by(id=amember.id).update({"points": points})
                session.commit()
                session.close()

                await ctx.send(
                    "You have gained " + str(pointvalue) + " point(s) {0.mention}!".format(amember) + " Total points: " + str(
                        points))

            else:
                ctx.send(" No points for you imposter... ")

    # Event Checkin
    @commands.command(pass_context=True)
    async def checkin(self,ctx):
        """Event Checkin and points."""

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
                ctx.trigger_typing()

                session.query(Member).filter_by(id=amember.id).update({"points": points})
                session.commit()
                session.close()

                await ctx.send(
                    "You have gained a checkin point {0.mention}!".format(
                        amember) + " Total points: " + str(
                        points))

        else:
            await ctx.send(" No points for you imposter... ")



def setup(bot):
        bot.add_cog(Points(bot))


