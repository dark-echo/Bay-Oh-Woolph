from discord.ext import commands
import discord
from bayohwoolph import bot

from config import Config

import logging
logger = logging.getLogger('bayohwoolph.cogs.mgmanager')

MULTIGAMETAGS = Config.config['MULTIGAMETAGS']

ROLE_MULTIGAME = MULTIGAMETAGS['ROLE_MULTIGAME']




Welcome_Message = """Congrats for joining the Multi-Game side of Dark Echo!!!
Below you will find a list of games that we have tags for. If you don't see a tag then please ping <@&551503870048862226> with the name of the game and we can look to add it.

Please use the following commands to add game tags:
$Minecraft
$SeaOfThieves
$RingOfElysium
$Fortnite
$ApexLegends
$TheDivision2
$WorldOfWarships


Any questions please ping <@&551503870048862226> with your question and we will get back to you asap.
"""




class Multigame:

    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def Multigame(self, ctx):
        """Adds Multigame tags"""

        mg_role = discord.utils.get(ctx.guild.roles, id=int(ROLE_MULTIGAME))
        member = ctx.message.author

        try:
            await member.add_roles(mg_role)
            await ctx.send(Welcome_Message)
        except:
            await ctx.send('Error Unable to add role')





def setup(bot):
    bot.add_cog(Multigame(bot))