#from config import config
from log import log
import re

class Module:
  def __init__(self, bot):
    """Module constructor"""
    self.bot = bot
    self.irc = bot.irc
    self.bot.bind('PRIVMSG', self.checklink)
    log("loaded link.py")

  def checklink(self, nick, type, chan, text):
    """Check if message contains link and send it"""
    if chan[0] != "#":
      return

    if re.search('\.g\/(.+)', text):
      q = re.search('\.g\/(\w+)', text).group(1)
      self.irc.send('PRIVMSG {0} :http://google.com/search?q={1}'.format(chan,q))
    elif re.search('\.w\/(.+)', text):
      q = re.search('\.w\/(\w+)', text).group(1)
      self.irc.send('PRIVMSG {0} :http://pl.wikipedia.org/wiki/{1}'.format(chan,q))
    elif re.search('\.ud#(.+)', text):
      q = re.search('\.ud#(\w+)', text).group(1)
      self.irc.send('PRIVMSG {0} :http://www.unrealircd.com/files/docs/unreal32docs.html#{1}'.format(chan,q))
    elif re.search('\.w\/(.+)', text):
      q = re.search('\.w\/(\w+)', text).group(1)
      self.irc.send('PRIVMSG {0} :http://pl.wikipedia.org/wiki/{1}'.format(chan,q))
    elif re.search('\.ch\/(.+)', text):
      q = re.search('\.ch\/(\w+)', text).group(1)
      self.irc.send('PRIVMSG {0} :http://chommik.eu/{1}'.format(chan,q))
    elif re.search('\.rch\/(.+)', text):
      q = re.search('\.rch\/(\w+)', text).group(1)
      self.irc.send('PRIVMSG {0} :http://r.chommik.eu/{1}'.format(chan,q))


