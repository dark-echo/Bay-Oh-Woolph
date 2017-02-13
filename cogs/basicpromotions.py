from discord.ext import commands
from utils import *
import discord
import asyncio

class Basicpromotions:
    """Leadership-only commands for promoting to basic membership roles."""
    
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    @commands.has_role('Leadership')
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
        """Give intro message to new cadet and assign them cadet role."""

        newcadetmsg = """
        **Welcome to Dark Echo, {0}!**

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

        If you stay active with us for a couple of weeks and haven't heard about a promotion to Officer, please remind the @Leadership.
        """

        yield from self.bot.type()

        # pull all the arguments into an array
        argmembers = [member1, member2, member3, member4, member5, member6, member7, member8, member9, member10, member11, member12, member13, member14, member15, member16, member17, member18, member19, member20 ]

        # and then filter out the None/empty items, so that we have only an array of things actually mentioned
        filter(None,argmembers)
        members = [i for i in argmembers if i is not None]

        # FIXME: make this a utilfunction.
        # Turns an array of members into a nicely formatted list of mentions.
        mentiontext = memberlist_to_mentionlist(members)

        yield from self.bot.say('Go check out <#146726509460193281>, ' + mentiontext + '.')

        cadetsmess = self.bot.get_channel('146726509460193281')

        yield from self.bot.send_message(cadetsmess,newcadetmsg.format(mentiontext))

        cadetrole = discord.Object(id=146725461727117314)
        
        for member in members:
            yield from self.bot.add_roles(member,cadetrole)

def setup(bot):
    bot.add_cog(Basicpromotions(bot))
