# -*- encoding: utf-8 -*-

from time import strftime
from config import config

class Module:
  def __init__(self, bot):
    """Module constructor"""
    self.bot = bot
    self.irc = bot.irc
    self.bot.bind('PRIVMSG',self.ctcp)
  def ctcp(self, src, type, dst, text):
    """Checks if message is CTCP"""
    if not text[0] == "\x01":
      return
    cmdtext = text[1:-1]
    cmd = cmdtext.split(' ')
    src = src.split('!')[0]
    if cmd[0] == "PING":
      self.irc.send("NOTICE " + src + " :\01PING {params}\01".format(params=' '.join(cmd[1:])))
    elif cmd[0] == 'VERSION':
      self.irc.send("NOTICE " + src + " :\01VERSION szynszyl\01")
    elif cmd[0] == 'TIME':
      self.irc.send("NOTICE " + src + " :\01TIME {time}\01".format(time=strftime(config['dateformat'])))