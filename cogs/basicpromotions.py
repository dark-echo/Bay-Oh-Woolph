from discord.ext import commands
from utils import *
import discord
import asyncio
from cogs.updateroster import UpdateRoster

from config import Config

import logging
logger = logging.getLogger('bayohwoolph.cogs.basicpromotions')

BASICPROMOTIONS = Config.config['BASICPROMOTIONS']

ROLE_CADET = BASICPROMOTIONS['ROLE_CADET']
ROLE_OFFICER = BASICPROMOTIONS['ROLE_OFFICER']
ROLE_PS4 = BASICPROMOTIONS['ROLE_PS4']
ROLE_PS4CADET = BASICPROMOTIONS['ROLE_PS4CADET']
ROLE_XBOX = BASICPROMOTIONS['ROLE_XBOX']
ROLE_XBOXCADET = BASICPROMOTIONS['ROLE_XBOXCADET']
ROLE_PC = BASICPROMOTIONS['ROLE_PC'] 

CADETS_MESS = BASICPROMOTIONS['CADETS_MESS']
PS4_ROOM = BASICPROMOTIONS['PS4_ROOM']
XBOX_ROOM = BASICPROMOTIONS['XBOX_ROOM']
OFFICERS_CLUB = BASICPROMOTIONS['OFFICERS_CLUB']
BOT_NOISE = BASICPROMOTIONS['bot_noise']

ROLE_MEMBER = BASICPROMOTIONS['ROLE_MEMBER']

NEWPCCADETMSG = """**Welcome to Dark Echo, {0}!**

**<:echoBlue:230423421983522816> Here are the basic steps to get started with Dark Echo: <:echoBlue:230423421983522816>**

-->Please read and make sure you understand the channel structure in <#146723400671428608>. 

1. If you use Inara, join us at <http://inara.cz/wing/300>
2. In the game, apply to the "Dark Echo" squadron.
3. Send in-game friend requests to the Echoes you see currently active on Discord and/or via in the in-game squadron.
4. Check <#161529165223428096> for current priorities.
5. Move your primary base of operations (any additional ships, etc) to Snodgrass Orbital in Disci.
6. Join the "Dark Echo" private group.

Note: You cannot get to Disci in a starter sidewinder.  You need 9.5LY jump range.  Upgrade from "E" to "D". We can help if you need it.

Please set an avatar image in Discord, as it greatly helps with telling people apart when using the in-game overlay.

If you stay active with us for a couple of weeks and haven't heard about a promotion to Officer, please remind the  Leadership.
"""

NEWPS4CADETMSG = """**Welcome to Dark Echo, {0}!**

**<:echoBlue:230423421983522816> Here are the basic steps to get started with Dark Echo: <:echoBlue:230423421983522816>**

-->Please read and make sure you understand the channel structure <#146723400671428608>.

1. If you use Inara, join us at http://inara.cz/wing/300
2. Send a PSN friend request to "Elite-DarkEcho".
3. Once PSN friend request is accepted: In the game, under "Friends and Private Groups",Send a friend request and request membership in the "Elite-DarkEcho" private group.
4. Check <#161529165223428096> for current priorities.
5. Move your primary base of operations (any additional ships, etc) to Snodgrass Orbital in Disci.
6. Set your ship id to [ECHO] or put [ECHO] in your ship name, whichever you prefer.


Note: You cannot get to Disci in a starter sidewinder.  You need 9.5LY jump range.  Upgrade Sidewinder or Eagle from "E" to "D"; or use a Hauler. If you're still having trouble, talk to us and somebody can help.

If you stay active with us for a couple of weeks and haven't heard about a promotion to Officer, please remind the Leadership.
"""

NEWXBOXCADETMSG = """**Welcome to Dark Echo, {0}!**

**<:echoBlue:230423421983522816> Here are the basic steps to get started with Dark Echo: <:echoBlue:230423421983522816>**

-->Please read and make sure you understand the channel structure in <#146723400671428608>.


1. If you use Inara, join us at http://inara.cz/wing/300
2. Send a XBOX Live friend request to "ED Dark Echo" and join the "Dark Echo" club.
3. Once XBOX Live friend request is accepted: In the game, under "Friends and Private Groups",request membership in the "ED Dark Echo" private group.
4. Check <#161529165223428096> for current priorities.
5. Move your primary base of operations (any additional ships, etc) to Snodgrass Orbital in Disci.
6. Set your ship id to [ECHO] or put [ECHO] in your ship name, whichever you prefer.



Note: You cannot get to Disci in a starter sidewinder.  You need 9.5LY jump range.  Upgrade Sidewinder or Eagle from "E" to "D"; or use a Hauler. If you're still having trouble, talk to us and somebody can help.

If you stay active with us for a couple of weeks and haven't heard about a promotion to Officer, please remind the Leadership.
"""

NEWOFFICERMSG = """**<:echoBlue:230423421983522816> Welcome to Dark Echo's Officer's Club, {0}!**

Dark Echos Dark Council believe that you are an asset to this organization, and has promoted you to a full member (Officer).

Optional but traditional and highly recommended: Please bring some sort of rare beverage to Snodgrass Orbital in Disci and share a screenshot of that run on the forums and/or in <#173953415280328704>.

If you use Inara, join us at <http://inara.cz/wing/300>.


"""

class Basicpromotions(commands.Cog):
    """Leadership/Recruiter commands for promoting to basic membership roles."""
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_any_role('Leadership','Recruiter')
    async def newpccadet(self,ctx,
        member1  : discord.Member = None, 
        member2  : discord.Member = None, 
        member3  : discord.Member = None, 
        member4  : discord.Member = None, 
        member5  : discord.Member = None, 
        member6  : discord.Member = None, 
        member7  : discord.Member = None, 
        member8  : discord.Member = None, 
        member9  : discord.Member = None, 
        member10 : discord.Member = None, 
        member11 : discord.Member = None, 
        member12 : discord.Member = None, 
        member13 : discord.Member = None, 
        member14 : discord.Member = None, 
        member15 : discord.Member = None, 
        member16 : discord.Member = None, 
        member17 : discord.Member = None, 
        member18 : discord.Member = None, 
        member19 : discord.Member = None, 
        member20 : discord.Member = None ):
        """Get new PC platform Cadet started."""

        await ctx.typing()

        # pull all the arguments into an array
        argmembers = [member1, member2, member3, member4, member5, member6, member7, member8, member9, member10, member11, member12, member13, member14, member15, member16, member17, member18, member19, member20 ]

        # and then filter out the None/empty items, so that we have only an array of things actually mentioned
        filter(None,argmembers)
        members = [i for i in argmembers if i is not None]

        memrole = discord.utils.get(ctx.guild.roles, id=int(ROLE_MEMBER))
        cadetrole = discord.utils.get(ctx.guild.roles, id=int(ROLE_CADET))
        pcrole = discord.utils.get(ctx.guild.roles, id=int(ROLE_PC))

        for member in members:
            try:
               await member.add_roles(cadetrole,memrole,pcrole)
            except Exception as e:
               await ctx.send('Unable to set PC Cadet role.')

        mentiontext = memberlist_to_mentionlist(members)

        cadetsmess = self.bot.get_channel(int(CADETS_MESS))
        await cadetsmess.send(NEWPCCADETMSG.format(mentiontext))
        await ctx.send('Go check out <#{}>, '.format(CADETS_MESS) + mentiontext + '.')

    @commands.command()
    @commands.has_any_role('Leadership','Recruiter')
    async def newps4cadet(self, ctx,
        member1  : discord.Member = None, 
        member2  : discord.Member = None, 
        member3  : discord.Member = None, 
        member4  : discord.Member = None, 
        member5  : discord.Member = None, 
        member6  : discord.Member = None, 
        member7  : discord.Member = None, 
        member8  : discord.Member = None, 
        member9  : discord.Member = None, 
        member10 : discord.Member = None, 
        member11 : discord.Member = None, 
        member12 : discord.Member = None, 
        member13 : discord.Member = None, 
        member14 : discord.Member = None, 
        member15 : discord.Member = None, 
        member16 : discord.Member = None, 
        member17 : discord.Member = None, 
        member18 : discord.Member = None, 
        member19 : discord.Member = None, 
        member20 : discord.Member = None):

        """Get new Playstation4 platform Cadet started."""

        await ctx.typing()

        # pull all the arguments into an array
        argmembers = [member1, member2, member3, member4, member5, member6, member7, member8, member9, member10, member11, member12, member13, member14, member15, member16, member17, member18, member19, member20 ]

        # and then filter out the None/empty items, so that we have only an array of things actually mentioned
        filter(None,argmembers)
        members = [i for i in argmembers if i is not None]

        memrole = discord.utils.get(ctx.guild.roles, id=int(ROLE_MEMBER))
        cadetrole = discord.utils.get(ctx.guild.roles, id=int(ROLE_CADET))
        ps4role =  discord.utils.get(ctx.guild.roles, id=int(ROLE_PS4))
        ps4cadet =  discord.utils.get(ctx.guild.roles, id=int(ROLE_PS4CADET))

        for member in members:
            try:
                await member.add_roles(cadetrole,memrole,ps4role,ps4cadet)
            except Exception as e:
                await ctx.send('Unable to set PS4 Cadet role.')

        mentiontext = memberlist_to_mentionlist(members)

        cadetsmess = self.bot.get_channel(int(CADETS_MESS))

        await cadetsmess.send(NEWPS4CADETMSG.format(mentiontext))
        await ctx.send('Go check out <#{}>, '.format(CADETS_MESS) + mentiontext + '.')
      
    @commands.command()
    @commands.has_any_role('Leadership','Recruiter')
    async def newxboxcadet(self, ctx,
        member1  : discord.Member = None,
        member2  : discord.Member = None,
        member3  : discord.Member = None,
        member4  : discord.Member = None,
        member5  : discord.Member = None,
        member6  : discord.Member = None,
        member7  : discord.Member = None,
        member8  : discord.Member = None,
        member9  : discord.Member = None,
        member10 : discord.Member = None,
        member11 : discord.Member = None,
        member12 : discord.Member = None,
        member13 : discord.Member = None,
        member14 : discord.Member = None,
        member15 : discord.Member = None,
        member16 : discord.Member = None,
        member17 : discord.Member = None,
        member18 : discord.Member = None,
        member19 : discord.Member = None,
        member20 : discord.Member = None ):
        """Get new xbox  platform Cadet started."""

        await ctx.typing()

        # pull all the arguments into an array
        argmembers = [member1, member2, member3, member4, member5, member6, member7, member8, member9, member10, member11, member12, member13, member14, member15, member16, member17, member18, member19, member20 ]

        # and then filter out the None/empty items, so that we have only an array of things actually mentioned
        filter(None,argmembers)
        members = [i for i in argmembers if i is not None]

        memrole = discord.utils.get(ctx.guild.roles, id=int(ROLE_MEMBER))
        cadetrole = discord.utils.get(ctx.guild.roles, id=int(ROLE_CADET))
        xboxrole = discord.utils.get(ctx.guild.roles, id=int(ROLE_XBOX))
        xboxcadet = discord.utils.get(ctx.guild.roles, id=int(ROLE_XBOXCADET))

        for member in members:
            try:
                await member.add_roles(cadetrole,memrole,xboxrole,xboxcadet)
            except Exception as e:
                await ctx.send('Unable to set Xbox Cadet role.')

        mentiontext = memberlist_to_mentionlist(members)

        cadetsmess = self.bot.get_channel(int(CADETS_MESS))


        await cadetsmess.send(NEWXBOXCADETMSG.format(mentiontext))
        await ctx.send('Go check out <#{}>, '.format(CADETS_MESS) + mentiontext + '.')

  

    @commands.command()
    @commands.has_role('Leadership')
    async def newofficer(self, ctx,
        member1  : discord.Member = None, 
        member2  : discord.Member = None, 
        member3  : discord.Member = None, 
        member4  : discord.Member = None, 
        member5  : discord.Member = None, 
        member6  : discord.Member = None, 
        member7  : discord.Member = None, 
        member8  : discord.Member = None, 
        member9  : discord.Member = None, 
        member10 : discord.Member = None, 
        member11 : discord.Member = None, 
        member12 : discord.Member = None, 
        member13 : discord.Member = None, 
        member14 : discord.Member = None, 
        member15 : discord.Member = None, 
        member16 : discord.Member = None, 
        member17 : discord.Member = None, 
        member18 : discord.Member = None, 
        member19 : discord.Member = None, 
        member20 : discord.Member = None ):
        """Give intro message to new officer and assign them Officer role."""

        await ctx.typing()

        # pull all the arguments into an array
        argmembers = [member1, member2, member3, member4, member5, member6, member7, member8, member9, member10, member11, member12, member13, member14, member15, member16, member17, member18, member19, member20 ]

        # and then filter out the None/empty items, so that we have only an array of things actually mentioned
        filter(None,argmembers)
        members = [i for i in argmembers if i is not None]

        pettyofficer = discord.utils.get(ctx.guild.roles, id=533299978567680011)
        officerrole = discord.utils.get(ctx.guild.roles, id=int(ROLE_OFFICER))
        cadetrole = discord.utils.get(ctx.guild.roles, id=int(ROLE_CADET))
        botnoise = self.bot.get_channel(int(BOT_NOISE))
        officersclub = self.bot.get_channel(int(OFFICERS_CLUB))
        
        for member in members:
            try:
                await member.add_roles(officerrole,pettyofficer)
            except Exception as e:
                await ctx.send('Unable to set Officer role.')

            cleannick = member_to_clean_nick(member)
            await botnoise.send('!addroster ' + cleannick)

        mentiontext = memberlist_to_mentionlist(members)

        # sleep for a second to make sure the role has gone through before sending messages that need it
        await asyncio.sleep(1)

        await officersclub.send(NEWOFFICERMSG.format(mentiontext))

        for member in members:
            await member.remove_roles(cadetrole)


async def setup(bot):
    await bot.add_cog(Basicpromotions(bot))
