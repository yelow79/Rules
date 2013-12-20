###
# Copyright (c) 2013, yelow79
# All rights reserved.
#
#
###

import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.ircmsgs as ircmsgs
import supybot.registry as registry
import supybot.callbacks as callbacks

try:
    from supybot.i18n import PluginInternationalization
    from supybot.i18n import internationalizeDocstring
    _ = PluginInternationalization('Rules')
            
except:
    # Placeholder that allows to run the plugin on a bot
    # without the i18n module
    _ = lambda x:x

class Rules(callbacks.Plugin):
    """Rules [<nick>] or Help [<nick>] - nick is optional, only to be used to
    send the rules/help to <nick>."""

    @wrap([additional('nick')])
    def rules(self, irc, msg, args, nick):
        """[<nick>] optional, only used to send the 
rules to another person"""
        
        if not nick:
            irc.reply(_('Sending you the Rules in an IRC Private Message'), prefixNick=True)
        elif nick:
            irc.reply(_('Sending %s the Rules in an IRC Private Message' % nick), prefixNick=False)
                    
        rules = """All Site Rules apply on this IRC 
With the addition of the following rules
1.
2.
3.
4.
\x1F\x0304Your actions here, can affect your account.\x03
\x1F\x0304Please follow the rules, we do not want to ban you!\x03"""
                                                                                                       
        for line in rules.split('\n'):
            irc.reply(line, to=nick, private=True, prefixNick=False)

Class = Rules

# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
