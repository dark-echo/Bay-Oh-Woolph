from discord.ext import commands
from utils import *
import discord
import asyncio

ROLE_CADET = '146725461727117314'
ROLE_OFFICER = '146724317785358337'

CADETS_MESS = '146726509460193281'
OFFICERS_CLUB = '146726934825533440'

NEWCADETMSG = """**Welcome to Dark Echo, {0}!**

**<:echoBlue:230423421983522816> Here are the basic steps to get started with Dark Echo: <:echoBlue:230423421983522816>**

1. Sign up for a forum account at <http://darkecho.org/forums/ucp.php?mode=register>
2. If you use Inara, join us at http://inara.cz/wing/300
3. In the game, under "Friends and Private Groups", request membership in the "Dark Echo" private group and send "Dark Echo" a friend request.
4. Send in-game friend requests to the Echoes you see currently active on Discord and/or via in the in-game private group.
5. Move your primary base of operations (any additional ships, etc) to Snodgrass Orbital in Disci.
6. Once your forum account is activated, look for "Getting Started" instructions there.

Note: You cannot get to Disci in a starter sidewinder.  You need a ship with at least a 9.5LY jump range.  Upgrade most components from "E" to "D" rated in a Sidewinder or Eagle or use a Hauler to make it. If you're still having trouble, talk to us and somebody can help.

Make sure you get that forum account set up, since that's what we use to track how long you've been a Cadet.

Please set an avatar image in Discord, as it greatly helps with telling people apart when using the in-game overlay.

If you stay active with us for a couple of weeks and haven't heard about a promotion to Officer, please remind the <@&146724062301913088>.
"""

NEWOFFICERMSG = """**<:echoBlue:230423421983522816> Welcome to Dark Echo's Officer's Club, {0}!**

Dark Echo <@&146724062301913088> believe that you are an asset to this organization, and has promoted you to a full member (Officer).

Optional but traditional and highly recommended: Please bring some sort of rare beverage to Snodgrass Orbital in Disci and share a screenshot of that run on the forums and/or in <#173953415280328704>.

A <@&235466370316238848> will update your forum permissions. Once your forum permissions are set up, make sure to:
* Read the latest Standing Orders: <http://www.darkecho.org/forums/viewforum.php?f=6>
* "Subscribe" to DE Urgent: <http://www.darkecho.org/forums/viewforum.php?f=7>
* and also "Ops": <http://www.darkecho.org/forums/viewforum.php?f=9>

If you use Inara, join us at <http://inara.cz/wing/300>

(Reminder to <@&146724062301913088>: Go do a "!addroster Nickname" in #allies, and update forum groups)

"""

class Basicpromotions:
    """Leadership-only commands for promoting to basic membership roles."""
    
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    @commands.has_role('Leadership')
    @commands.has_role('Recruiter')
    @asyncio.coroutine
    def newcadet(self,
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
        """Give intro message to new cadet and assign them Cadet role."""

        yield from self.bot.type()

        # pull all the arguments into an array
        argmembers = [member1, member2, member3, member4, member5, member6, member7, member8, member9, member10, member11, member12, member13, member14, member15, member16, member17, member18, member19, member20 ]

        # and then filter out the None/empty items, so that we have only an array of things actually mentioned
        filter(None,argmembers)
        members = [i for i in argmembers if i is not None]

        cadetrole = discord.Object(id=ROLE_CADET)
        for member in members:
            yield from self.bot.add_roles(member,cadetrole)

        mentiontext = memberlist_to_mentionlist(members)

        cadetsmess = self.bot.get_channel(CADETS_MESS)


        yield from self.bot.send_message(cadetsmess,NEWCADETMSG.format(mentiontext))
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
        
        for member in members:
            yield from self.bot.add_roles(member,officerrole)

        mentiontext = memberlist_to_mentionlist(members)

        officersclub = self.bot.get_channel(OFFICERS_CLUB)

        # sleep for a second to make sure the role has gone through before sending messages that need it
        yield from asyncio.sleep(1)

        yield from self.bot.send_message(officersclub,NEWOFFICERMSG.format(mentiontext))

        for member in members:
            yield from self.bot.remove_roles(member,cadetrole)


def setup(bot):
    bot.add_cog(Basicpromotions(bot))
