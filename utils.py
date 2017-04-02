import logging
import re
logger = logging.getLogger('bayohwoolph.utils')

# Turns a list of members into a nicely formatted string
def memberlist_to_mentionlist(members):
    mentiontext = ''
    if len(members) == 0:
        mentiontext = 'Nobody'
    elif len(members) == 1:
        mentiontext = members[0].mention
    elif len(members) > 1:
        mentions = [i.mention for i in members]
        mentiontext = ', '.join(mentions[:-1])
        mentiontext = mentiontext + ' and ' + mentions[-1]
    return mentiontext

emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00010000-\U0010ffff"  # Seriously huge range that covers emojis
                           "]+", flags=re.UNICODE)

tag_pattern_paren = re.compile("\s*\(.+\)\s*$")
tag_pattern_bracket = re.compile("\s*\[.+\]\s*$")

def member_to_clean_nick(member):
    # Get the server nick or global name:
    nick = member.display_name
    logger.debug('nick:initial: '+ nick)

    # Strip emojis off:
    nick = emoji_pattern.sub(r'', nick)
    logger.debug('nick:emoji: '+ nick)
    
    # Strip (paren) tags off:    
    nick = tag_pattern_paren.sub(r'', nick)
    logger.debug('nick:paren: '+ nick)

    # Strip [bracket] tags off:    
    nick = tag_pattern_bracket.sub(r'', nick)
    logger.debug('nick:bracket: '+ nick)

    # Strip excess whitespace off:
    nick = nick.strip()
    logger.debug('nick:strip: ' + nick)
    
    return nick
