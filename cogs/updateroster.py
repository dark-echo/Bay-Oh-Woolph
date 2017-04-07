from discord.ext import commands
from utils import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import *
from member import Base, Member, Rank
from utility.dbproc import Baydb
from bayohwoolph import bot
import discord
import asyncio
import logging

import logging
logger = logging.getLogger('bayohwoolph.cogs.updateroster')

from config import Config

UPDATEROSTER = Config.config['UPDATEROSTER']

ROLE_MEMBER = UPDATEROSTER['ROLE_MEMBER']
MOD_LOG = UPDATEROSTER['MOD_LOG']

session = Baydb.session
conn = Baydb.conn


#Command to Update Roster
class UpdateRoster:
    """Admin tools for updating bot's internal roster info."""

    def __init__(self, bot):
        self.bot = bot
    #assign bot to bayohwoolpbot


    @commands.command()
    @commands.has_role('Leadership')
    @asyncio.coroutine
    def updateroster(self):
        """Updates the Database"""
        conn.begin()
        mod = self.bot.get_channel(MOD_LOG)

        memberrole = discord.Object(id=ROLE_MEMBER)

        count = 0
        # Intialize array
        listOfMembers = []

        yield from self.bot.type()
        # Add members to array
        for themember in self.bot.get_all_members():
            arole = [role for role in themember.roles if role.id == memberrole.id]
            if arole:
                if arole[0].id == memberrole.id:
                    listOfMembers.append(
                        Member(int(themember.id), str(themember.name), str(themember.nick),str(themember.top_role),int(themember.top_role.id)))

        for amember in listOfMembers:
            q = session.query(exists().where(Member.id == amember.id)).scalar()
            if q:
                session.merge(amember)
                # Rework and put this in a seperate command when points have to be loaded in due to manual rank change.
                ''' stmt = update(Member). \
                        where(Member.id == amember.id). \
                        values(points=(select([Rank.pointValue])).where(
                        Member.rankId == Rank.rankId and Member.role != "Cadet" and Member.points == 0 | Member.points == null))

                    conn.execute(stmt) '''
            else:
                session.add(amember)
                count = count + 1
        try:
            session.commit()
            if count != 0:
                yield from self.bot.say("DB successfully updated." + " Number of members inserted: " + str(count))
            else:
                yield from self.bot.say("DB successfully updated. No new members inserted.")
        except:
            session.rollback()
            yield from self.bot.send_message(mod, "Insertion failure")
        session.close()
        conn.close()

    #Update Roster on newcadet
    @bot.event
    @asyncio.coroutine
    def on_message(self,message):
        mod = self.bot.get_channel(MOD_LOG)

        if message.content.startswith('$newcadet'):
            yield from asyncio.sleep(5)
            memberrole = discord.Object(id=ROLE_MEMBER)

            count = 0
            # Intialize array
            listOfMembers = []

            # Add members to array
            for themember in self.bot.get_all_members():
                arole = [role for role in themember.roles if role.id == memberrole.id]
                if arole:
                    if arole[0].id == memberrole.id:
                        listOfMembers.append(
                            Member(int(themember.id), str(themember.name), str(themember.nick), str(themember.top_role),int(themember.top_role.id)))

            for amember in listOfMembers:
                q = session.query(exists().where(Member.id == amember.id)).scalar()
                if q:
                    session.merge(amember)

                else:
                    session.add(amember)
                    count = count + 1

            try:
                session.commit()


                if count != 0:
                    yield from self.bot.send_message(mod, "DB successfully updated." + " Number of members inserted: " + str(count))
                else:
                    yield from self.bot.send_message(mod, "DB successfully updated. No new members inserted.")

            except:
                session.rollback()
                yield from self.bot.send_message(mod, "Insertion failure")
            session.close()
            conn.close()


def setup(bot):
    bot.add_cog(UpdateRoster(bot))