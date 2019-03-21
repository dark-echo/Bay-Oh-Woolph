from discord.ext import commands
import discord
from bayohwoolph import bot

from config import Config

import logging
logger = logging.getLogger('bayohwoolph.cogs.mgmanager')

MULTIGAMETAGS = Config.config['MULTIGAMETAGS']

ROLE_MULTIGAME = MULTIGAMETAGS['ROLE_MULTIGAME']
ROLE_APEX = MULTIGAMETAGS['ROLE_APEX']
ROLE_WOW = MULTIGAMETAGS['ROLE_WOW']
ROLE_TCTD2 = MULTIGAMETAGS['ROLE_TCTD2']
ROLE_FORTNITE = MULTIGAMETAGS['ROLE_FORTNITE']
ROLE_ROE = MULTIGAMETAGS['ROLE_ROE']
ROLE_SOT = MULTIGAMETAGS['ROLE_SOT']
ROLE_MINECRAFT = MULTIGAMETAGS['ROLE_MINECRAFT']






Welcome Message = """Congrats for joining the Multi-Game side of Dark Echo!!!
Below you will find a list of games that we have tags for. If you don't see a tag then please ping <@&551503870048862226 with the name of the game and we can look to add it.

Minecraft
Sea Of Thieves
Ring of Elysium
Fortnite
Apex Legends
The Division 2
World of Warships




Please use $"gamename" to add game tags to yourself doing so allows you to see any game specific channels.

Any questions please ping <@&551503870048862226 with your question and we will get back to you asap.
"""


class Multigame:

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def Multigame(self, ctx):

        mg_role = discord.utils.get(ctx.guild.roles, id=int(ROLE_MULTIGAME))



