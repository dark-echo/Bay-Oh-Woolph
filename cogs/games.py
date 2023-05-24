from discord.ext import commands
import discord

from config import Config

import logging
logger = logging.getLogger('bayohwoolph.cogs.mgmanager')

MULTIGAMETAGS = Config.config['MULTIGAMETAGS']


ROLE_APEX = MULTIGAMETAGS['ROLE_APEX']
ROLE_WOW = MULTIGAMETAGS['ROLE_WOW']
ROLE_TCTD2 = MULTIGAMETAGS['ROLE_TCTD2']
ROLE_FORTNITE = MULTIGAMETAGS['ROLE_FORTNITE']
ROLE_ROE = MULTIGAMETAGS['ROLE_ROE']
ROLE_SOT = MULTIGAMETAGS['ROLE_SOT']
ROLE_MINECRAFT = MULTIGAMETAGS['ROLE_MINECRAFT']


tags_added = """"Congrats your are the proud owner of a new game tag"""


class Games(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def Apex(self, ctx):
        """Adds Apex Legends tags"""

        apex_role = discord.utils.get(ctx.guild.roles, id=int(ROLE_APEX))
        member = ctx.message.author

        try:
            await member.add_roles(apex_role)
            await ctx.send(tags_added)
        except:
            await ctx.send('Error Unable to add role')

    @commands.command()
    async def WorldOfWarships(self, ctx):
        """Adds World of Warships tags"""

        wow_role = discord.utils.get(ctx.guild.roles, id=int(ROLE_WOW))
        member = ctx.message.author

        try:
            await member.add_roles(wow_role)
            await ctx.send(tags_added)
        except:
            await ctx.send('Error Unable to add role')

    @commands.command()
    async def TheDivision2(self, ctx):
        """Adds The Division 2 tags"""

        td2_role = discord.utils.get(ctx.guild.roles, id=int(ROLE_TCTD2))
        member = ctx.message.author

        try:
            await member.add_roles(td2_role)
            await ctx.send(tags_added)
        except:
            await ctx.send('Error Unable to add role')

    @commands.command()
    async def Fortnite(self, ctx):
        """Adds Fortnite tags"""

        fort_role = discord.utils.get(ctx.guild.roles, id=int(ROLE_FORTNITE))
        member = ctx.message.author

        try:
            await member.add_roles(fort_role)
            await ctx.send(tags_added)
        except:
            await ctx.send('Error Unable to add role')

    @commands.command()
    async def RingsOfElysium(self, ctx):
        """Adds Rings of Elysium tags"""

        roe_role = discord.utils.get(ctx.guild.roles, id=int(ROLE_ROE))
        member = ctx.message.author

        try:
            await member.add_roles(roe_role)
            await ctx.send(tags_added)
        except:
            await ctx.send('Error Unable to add role')

    @commands.command()
    async def SeaOfThieves(self, ctx):
        """Adds Sea Of Thieves tags"""

        sot_role = discord.utils.get(ctx.guild.roles, id=int(ROLE_SOT))
        member = ctx.message.author

        try:
            await member.add_roles(sot_role)
            await ctx.send(tags_added)
        except:
            await ctx.send('Error Unable to add role')

    @commands.command()
    async def Minecraft(self, ctx):
        """Adds Minecraft tags"""

        mine_role = discord.utils.get(ctx.guild.roles, id=int(ROLE_MINECRAFT))
        member = ctx.message.author

        try:
            await member.add_roles(mine_role)
            await ctx.send(tags_added)
        except:
            await ctx.send('Error Unable to add role')




async def setup(bot):
    await bot.add_cog(Games(bot))
