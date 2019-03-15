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

import datetime
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
    async def updateroster(self,ctx):
        """Updates the Database"""

        mod = self.bot.get_channel(int(MOD_LOG))

        memberrole = discord.utils.get(ctx.guild.roles, id=int(ROLE_MEMBER))

        count = 0
        # Intialize array
        listOfMembers = []

        await ctx.invoke_typing()

        
        # Add members to array
        for themember in self.bot.get_all_members():
            arole = [role for role in themember.roles if role.id == memberrole.id]
            if arole:
                if arole[0].id == memberrole.id:
                    listOfMembers.append(
                        Member(int(themember.id), str(themember.name), str(themember.nick),str(themember.top_role),int(themember.top_role.id),(themember.joined_at)))

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
                await ctx.send("DB successfully updated." + " Number of members inserted: " + str(count))
            else:
                await ctx.send("DB successfully updated. No new members inserted.")
        except:
            session.rollback()
            await mod.send("Insertion failure")
        session.close()
        conn.close()

    #Update Roster on newcadet, newpccadet, newps4cadet, newofficer, etc...
    @bot.event
    async def on_message(self,ctx, message):
        mod = self.bot.get_channel(int(MOD_LOG))

        if message.content.startswith('$new'):
            await asyncio.sleep(5)
            memberrole = discord.utils.get(ctx.guild.roles, id=int(ROLE_MEMBER))

            count = 0
            # Intialize array
            listOfMembers = []

            # Add members to array
            for themember in self.bot.get_all_members():
                arole = [role for role in themember.roles if role.id == memberrole.id]
                if arole:
                    if arole[0].id == memberrole.id:
                        listOfMembers.append(
                            Member(int(themember.id), str(themember.name), str(themember.nick), str(themember.top_role),int(themember.top_role.id),themember.joined_at))

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
                    await mod.send("DB successfully updated." + " Number of members inserted: " + str(count))
                else:
                    await mod.send("DB successfully updated. No new members inserted.")

            except:
                session.rollback()
                await mod.send("Insertion failure")
            session.close()
            conn.close()

            
    @commands.command()
    @commands.has_role('Leadership')
    async def cadetcheck(self,ctx):
       """Check for new cadets to be promoted """
       await ctx.send("Cadets to be promoted:")
       stmt = select([Member.globalName,Member.nickname,Member.role,Member.joinDate]).where(Member.role=='Cadet')
       result = conn.execute(stmt) 
       for row in result:
             await ctx.send(row) 
      
        

def setup(bot):
    bot.add_cog(UpdateRoster(bot))
