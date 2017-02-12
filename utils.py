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

