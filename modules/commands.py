# -*- encoding: utf-8 -*-

from modules import BaseModule
from config import config
import re

class Module(BaseModule):
  def __init__(self, bot):
    """Module constructor"""
    self.bot = bot
    self.irc = bot.irc
    self.bot.bind("PRIVMSG",self.privmsg)

  def privmsg(self, src, type, dst, text):
    """PRIVMSG handler"""
    mycmds = ['.die','.rehash','.raw','.join','.part','.py']

    args = text.split(' ')
    if not args[0] in mycmds:
      return

    if not self.is_admin(src):
      self.irc.send('PRIVMSG {dst} :{src}: Spierdalaj.'.format(dst=dst,src=src))
      return
    
    src = re.match('(.+?)!',src).group(1)

    if args[0] == '.rehash':
      self.bot.reloadmodules()
      if self.is_channel(dst):
        self.irc.send('PRIVMSG {dst} :{src}: Reload modułów.'.format(dst=dst,src=src))
      else:
        self.irc.send('PRIVMSG {src} :Reload modułów.'.format(src=src))
    elif args[0] == '.die':
      self.irc.send('PRIVMSG {dst} :{src}: Shutdown.'.format(dst=dst,src=src))
      self.bot.shutdown()
    elif args[0] == '.join':
      self.irc.send('JOIN {chan}'.format(chan=args[1]))
    elif args[0] == '.part':
      if len(args) > 1:
        self.irc.send('PART {chan}'.format(chan=args[1]))
      else:
        if self.is_channel(dst):
          self.irc.send('PART {chan}'.format(chan=dst))
    elif args[0] == '.raw':
      if len(args) > 1:
        self.irc.send('{text}'.format(text=' '.join(args[1:])))
      else:
        self.irc.send('PRIVMSG {dst} :{src}: Brak argumentu.'.format(dst=dst,src=src))
    elif args[0] == '.py':
      if len(args) > 1:
        self.irc.send('PRIVMSG {src} :>>> {text}'.format(text=eval(' '.join(args[1:])), dst=dst, src=src))
      else:
        self.irc.send('PRIVMSG {dst} :{src}: Brak argumentu.'.format(dst=dst,src=src))