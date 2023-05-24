from discord.ext import commands
from utils import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import *
from member import Base, Member
from utilities.dbproc import Baydb
from utils import member_to_clean_nick
from beautifultable import BeautifulTable
import discord
import asyncio
import logging

from datetime import datetime,timedelta
logger = logging.getLogger('bayohwoolph.cogs.updateroster')

from config import Config

UPDATEROSTER = Config.config['UPDATEROSTER']

ROLE_MEMBER = UPDATEROSTER['ROLE_MEMBER']
MOD_LOG = UPDATEROSTER['MOD_LOG']

session = Baydb.session
conn = Baydb.conn
table1 = BeautifulTable()
table2 = BeautifulTable()


#Command to Update Roster
class UpdateRoster(commands.Cog):
    """Admin tools for updating bot's internal roster info."""

    def __init__(self, bot):
        self.bot = bot
    #assign bot to bayohwoolpbot

    def check_if_infinite(ctx):
        return ctx.message.author.id == 145331384162975744 

    @commands.command()
    @commands.has_any_role('Leadership')
    async def updateroster(self,ctx):
        """Updates the Database"""

        mod = self.bot.get_channel(int(MOD_LOG))

        memberrole = discord.utils.get(ctx.guild.roles, id=int(ROLE_MEMBER))

        count = 0
        count2 = 0
        # Intialize array
        listOfMembers = []



        
        # Add members to array
        for themember in self.bot.get_all_members():
            arole = [role for role in themember.roles if role.id == memberrole.id]
            if arole:
                if arole[0].id == memberrole.id:
                    listOfMembers.append(
                        Member(int(themember.id), str(themember.name), str(member_to_clean_nick(themember)),str(themember.top_role),int(themember.top_role.id),(themember.joined_at)))
        conn = Baydb.conn.connect()
        for amember in listOfMembers:
            q = session.query(exists().where(Member.id == amember.id))
            if q:
                session.merge(amember)
                count2 += 1
            else:
                session.add(amember)
                count += 1
        try:
            session.commit()
            if count > 0:
                await ctx.send("DB successfully updated." + " Number of members inserted: " + str(count))
            elif count2 > 0:
                await ctx.send("DB successfully updated." + " Number of members updated: " + str(count2))
            else:
                await ctx.send("DB successfully updated. No new members inserted or updated.")
        except:
            session.rollback()
            await mod.send("Insertion failure")
        session.close()
        conn.close()

    #Cacet check command, prints out table of eligible promotions.        
    @commands.command()
    @commands.has_role('Leadership')
    async def cadetcheck(self,ctx):
       """Check for new cadets to be promoted """
       
       table1 = BeautifulTable()
       table2 = BeautifulTable()

       count1 = 0
       count2 = 0
       #2 Weeks Promotion Code
       table1.column_headers = ["GlobalName", "NickName", "Role", "JoinDate"]
       await ctx.send("Cadets to be promoted 2 Weeks Standard:")

       #Stmt formation for 2 weeks since joining server
       stmt = select([Member.globalName, Member.nickname, Member.role, Member.joinDate])\
           .where(and_ (Member.role == 'Cadet', cast(Member.joinDate,Date) <= (datetime.now().date() - timedelta(14))))

       result1 = conn.execute(stmt)

       #Check if result rowcount  returns rows from db then process

       # Iterate through result set and append to table2
       for row in result1:
            table1.append_row([row['globalName'], row['nickname'], row['role'],str(row['joinDate'].strftime("%b %d %Y"))])
            count1+=1

       str1 = "```"+str(table1)+"```"
       if count1 !=0:
           await ctx.send(str1)

       #1 Weeks Promotion Code
       table2.column_headers = ["GlobalName", "NickName", "Role", "JoinDate"]
       await ctx.send("Cadets to be possibly promoted 1 Week Awesome:")

       #Stmt formation for 1 week since joining server
       stmt2 = select([Member.globalName, Member.nickname, Member.role, Member.joinDate])\
           .where(and_ (Member.role == 'Cadet', cast(Member.joinDate,Date) <= (datetime.now().date() - timedelta(7))))
       result2 = conn.execute(stmt2)

       #Iterate through result set and append to table2
       for row in result2:
               table2.append_row([row['globalName'], row['nickname'], row['role'],str(row['joinDate'].strftime("%b %d %Y"))])
               count2+=1

       ##Check if result is not empty then send.
       str2 = "```"+str(table2)+"```"
       if count2 !=0:
           await ctx.send(str2)



async def setup(bot):
    await bot.add_cog(UpdateRoster(bot))
