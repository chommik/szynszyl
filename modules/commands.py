# -*- encoding: utf-8 -*-

from config import config
import re

class Module:
  def __init__(self, bot):
    """Module constructor"""
    self.bot = bot
    self.irc = bot.irc
    self.bot.bind("PRIVMSG",self.privmsg)

  def privmsg(self, src, type, dst, text):
    """PRIVMSG handler"""
    if text[0] != '.':
      return

    if text.split(' ')[0] != ".die" and text.split(' ')[0] != ".rehash":
      return


    if not src in config['admins']:
      self.irc.send('PRIVMSG {dst} :{src}: Spierdalaj.'.format(dst=dst,src=src))
      return
    
    src = re.match('(.+?)!',src).group(1)

    if text == '.rehash':
      self.bot.reloadmodules()
      self.irc.send('PRIVMSG {dst} :{src}: Reload modułów.'.format(dst=dst,src=src))
    elif text == '.die':
      self.irc.send('PRIVMSG {dst} :{src}: Shutdown.'.format(dst=dst,src=src))
      self.bot.shutdown()
      
