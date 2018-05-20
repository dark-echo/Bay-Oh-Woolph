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

-->Please read and make sure you understand the channel structure in <#382677822436671490>. 

1. If you use Inara, join us at http://inara.cz/wing/300
2. In the game, under "Friends and Private Groups", request membership in the "Dark Echo" private group and send "Dark Echo" a friend request.
3. Send in-game friend requests to the Echoes you see currently active on Discord and/or via in the in-game private group.
4. Check <#161529165223428096> for current priorities.
5. Move your primary base of operations (any additional ships, etc) to Snodgrass Orbital in Disci.
6. Set your ship id to [ECHO] or put [ECHO] in your ship name, whichever you prefer. 

Note: You cannot get to Disci in a starter sidewinder.  You need 9.5LY jump range.  Upgrade Sidewinder or Eagle from "E" to "D"; or use a Hauler. If you're still having trouble, talk to us and somebody can help.

Make sure you get that forum account set up, since that's what we use to share information. Also check your welcome email, there is an optional and yet fun way to make your trip to Disci worthwhile.

Please set an avatar image in Discord, as it greatly helps with telling people apart when using the in-game overlay.

If you stay active with us for a couple of weeks and haven't heard about a promotion to Officer, please remind the  Leadership.
"""

NEWPS4CADETMSG = """**Welcome to Dark Echo, {0}!**

**<:echoBlue:230423421983522816> Here are the basic steps to get started with Dark Echo: <:echoBlue:230423421983522816>**

-->Please read and make sure you understand the channel structure <#382677822436671490>.

1. If you use Inara, join us at http://inara.cz/wing/300
2. Send a PSN friend request to "Elite-DarkEcho".
3. Once PSN friend request is accepted: In the game, under "Friends and Private Groups",Send a friend request and request membership in the "Elite-DarkEcho" private group.
4. Check <#161529165223428096> for current priorities.
5. Move your primary base of operations (any additional ships, etc) to Snodgrass Orbital in Disci.
6. Set your ship id to [ECHO] or put [ECHO] in your ship name, whichever you prefer.


Note: You cannot get to Disci in a starter sidewinder.  You need 9.5LY jump range.  Upgrade Sidewinder or Eagle from "E" to "D"; or use a Hauler. If you're still having trouble, talk to us and somebody can help.

Make sure you get that forum account set up, since that's what we use to share information. Also check your welcome email, there is an optional and yet fun way to make your trip to Disci worthwhile.

If you stay active with us for a couple of weeks and haven't heard about a promotion to Officer, please remind the Leadership.
"""

NEWXBOXCADETMSG = """**Welcome to Dark Echo, {0}!**

**<:echoBlue:230423421983522816> Here are the basic steps to get started with Dark Echo: <:echoBlue:230423421983522816>**

-->Please read and make sure you understand the channel structure in <#382677822436671490>.


1. If you use Inara, join us at http://inara.cz/wing/300
2. Send a XBOX Live friend request to "ED Dark Echo" and join the "Dark Echo" club.
3. Once XBOX Live friend request is accepted: In the game, under "Friends and Private Groups",request membership in the "ED Dark Echo" private group.
4. Check <#161529165223428096> for current priorities.
5. Move your primary base of operations (any additional ships, etc) to Snodgrass Orbital in Disci.
6. Set your ship id to [ECHO] or put [ECHO] in your ship name, whichever you prefer.



Note: You cannot get to Disci in a starter sidewinder.  You need 9.5LY jump range.  Upgrade Sidewinder or Eagle from "E" to "D"; or use a Hauler. If you're still having trouble, talk to us and somebody can help.

Make sure you get that forum account set up, since that's what we use to share information. Also check your welcome email, there is an optional and yet fun way to make your trip to Disci worthwhile.

If you stay active with us for a couple of weeks and haven't heard about a promotion to Officer, please remind the Leadership.
"""

NEWOFFICERMSG = """**<:echoBlue:230423421983522816> Welcome to Dark Echo's Officer's Club, {0}!**

Dark Echo <@&146724062301913088> believe that you are an asset to this organization, and has promoted you to a full member (Officer).

Optional but traditional and highly recommended: Please bring some sort of rare beverage to Snodgrass Orbital in Disci and share a screenshot of that run on the forums and/or in <#173953415280328704>.

A <@&235466370316238848> will update your forum permissions. Once your forum permissions are set up, make sure to:

If you use Inara, join us at <http://inara.cz/wing/300>.

Have you checked out all the useful stuff in the forums?


"""

class Basicpromotions:
    """Leadership/Recruiter commands for promoting to basic membership roles."""
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_any_role('Leadership','Recruiter')
    @asyncio.coroutine
    def newpccadet(self,
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

        yield from self.bot.type()

        # pull all the arguments into an array
        argmembers = [member1, member2, member3, member4, member5, member6, member7, member8, member9, member10, member11, member12, member13, member14, member15, member16, member17, member18, member19, member20 ]

        # and then filter out the None/empty items, so that we have only an array of things actually mentioned
        filter(None,argmembers)
        members = [i for i in argmembers if i is not None]

        memrole = discord.Object(id=ROLE_MEMBER)
        cadetrole = discord.Object(id=ROLE_CADET)
        pcrole = discord.Object(id=ROLE_PC) 

        for member in members:
            try:
                yield from self.bot.add_roles(member,cadetrole,memrole,pcrole)
            except Exception as e:
                yield from self.bot.say('Unable to set Officer role.')

        mentiontext = memberlist_to_mentionlist(members)

        cadetsmess = self.bot.get_channel(CADETS_MESS)

        yield from self.bot.send_message(cadetsmess,NEWPCCADETMSG.format(mentiontext))
        yield from self.bot.say('Go check out <#{}>, '.format(CADETS_MESS) + mentiontext + '.')

    @commands.command()
    @commands.has_any_role('Leadership','Recruiter')
    @asyncio.coroutine
    def newps4cadet(self,
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
        """Get new Playstation4 platform Cadet started."""

        yield from self.bot.type()

        # pull all the arguments into an array
        argmembers = [member1, member2, member3, member4, member5, member6, member7, member8, member9, member10, member11, member12, member13, member14, member15, member16, member17, member18, member19, member20 ]

        # and then filter out the None/empty items, so that we have only an array of things actually mentioned
        filter(None,argmembers)
        members = [i for i in argmembers if i is not None]

        memrole = discord.Object(id=ROLE_MEMBER)
        cadetrole = discord.Object(id=ROLE_CADET)
        ps4role = discord.Object(id=ROLE_PS4)
        ps4cadet = discord.Object(id=ROLE_PS4CADET)

        for member in members:
            try:
                yield from self.bot.add_roles(member,cadetrole,memrole,ps4role,ps4cadet)
            except Exception as e:
                yield from self.bot.say('Unable to set Officer role.')

        mentiontext = memberlist_to_mentionlist(members)

        cadetsmess = self.bot.get_channel(CADETS_MESS)
        ps4room    = self.bot.get_channel(PS4_ROOM)

        yield from self.bot.send_message(cadetsmess,NEWPS4CADETMSG.format(mentiontext))
        yield from self.bot.send_message(ps4room,'<@&269222564826447872> Please send an in-game friend request to ' + mentiontext)
        yield from self.bot.say('Go check out <#{}>, '.format(CADETS_MESS) + mentiontext + '.')
      
    @commands.command()
    @commands.has_any_role('Leadership','Recruiter')
    @asyncio.coroutine
    def newxboxcadet(self,
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

        yield from self.bot.type()

        # pull all the arguments into an array
        argmembers = [member1, member2, member3, member4, member5, member6, member7, member8, member9, member10, member11, member12, member13, member14, member15, member16, member17, member18, member19, member20 ]

        # and then filter out the None/empty items, so that we have only an array of things actually mentioned
        filter(None,argmembers)
        members = [i for i in argmembers if i is not None]

        memrole = discord.Object(id=ROLE_MEMBER)
        cadetrole = discord.Object(id=ROLE_CADET)
        xboxrole = discord.Object(id=ROLE_XBOX)
        xboxcadet = discord.Object(id=ROLE_XBOXCADET)

        for member in members:
            try:
                yield from self.bot.add_roles(member,cadetrole,memrole,xboxrole,xboxcadet)
            except Exception as e:
                yield from self.bot.say('Unable to set Officer role.')

        mentiontext = memberlist_to_mentionlist(members)

        cadetsmess = self.bot.get_channel(CADETS_MESS)
        xboxroom    = self.bot.get_channel(XBOX_ROOM)

        yield from self.bot.send_message(cadetsmess,NEWXBOXCADETMSG.format(mentiontext))
        yield from self.bot.send_message(xboxroom,'<@&161285579894554635> Please send an in-game friend request to ' + mentiontext)
        yield from self.bot.say('Go check out <#{}>, '.format(CADETS_MESS) + mentiontext + '.')

  

    @commands.command()
    @commands.has_role('Leadership')
    @asyncio.coroutine
    def newofficer(self,
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

        yield from self.bot.type()

        # pull all the arguments into an array
        argmembers = [member1, member2, member3, member4, member5, member6, member7, member8, member9, member10, member11, member12, member13, member14, member15, member16, member17, member18, member19, member20 ]

        # and then filter out the None/empty items, so that we have only an array of things actually mentioned
        filter(None,argmembers)
        members = [i for i in argmembers if i is not None]

        officerrole = discord.Object(id=ROLE_OFFICER)
        cadetrole = discord.Object(id=ROLE_CADET)
        officersclub = self.bot.get_channel(OFFICERS_CLUB)
        botnoise = self.bot.get_channel(BOT_NOISE)
        
        for member in members:
            try:
                yield from self.bot.add_roles(member,officerrole)
            except Exception as e:
                yield from self.bot.say('Unable to set Officer role.')

            cleannick = member_to_clean_nick(member)
            yield from self.bot.send_message(botnoise, '!addroster ' + cleannick)

        mentiontext = memberlist_to_mentionlist(members)

        # sleep for a second to make sure the role has gone through before sending messages that need it
        yield from asyncio.sleep(1)

        yield from self.bot.send_message(officersclub,NEWOFFICERMSG.format(mentiontext))

        yield from self.bot.send_message(botnoise,"!whois -r -d -role 'Officer' -nick")

        for member in members:
            yield from self.bot.remove_roles(member,cadetrole)


def setup(bot):
    bot.add_cog(Basicpromotions(bot))
