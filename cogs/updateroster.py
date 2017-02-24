from discord.ext import commands
from utils import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import exists
from member import Base, Member
from utility.dbproc import Baydb
import discord
import asyncio
import logging

session = Baydb.session

ROLE_MEMBER = '284029774513569793'

MOD_LOG = '274619518662344704'



#Command to Update Roster
class UpdateRoster:


    def __init__(self, bot):
        self.bot = bot
    #assign bot to bayohwoolpbot


    @commands.command()
    @commands.has_role('Leadership')
    @asyncio.coroutine
    def updateroster(self):
        """Updates the Database"""
        mod = self.bot.get_channel(MOD_LOG)

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
                        Member(int(themember.id), str(themember.name), str(themember.nick),str(themember.top_role),int(themember.top_role.id)))

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
                yield from self.bot.send_message(mod,"DB successfully updated." + " Number of members inserted: " + str(count))


            else:
                yield from self.bot.send_message(mod, "DB successfully updated. No new members inserted.")

        except:
            session.roleback()

        session.close()

    #Update Roster on newcadet
    @commands.Bot.event()
    @asyncio.coroutine
    def on_message(self,message):
        mod = self.bot.get_channel(MOD_LOG)

        if message.content.startswith('$newcadet'):
            yield from self.bot(asyncio.sleep(5))
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
                    yield from  self.bot.send_message(mod, "DB successfully updated. No new members inserted.")

            except:
                session.roleback()
                yield from  self.bot.send_message(mod, "Insertion failure")
            session.close()




def setup(bbot):
    bbot.add_cog(UpdateRoster(bbot))