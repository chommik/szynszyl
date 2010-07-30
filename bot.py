import irc
import re
from config import *
import _thread

class Bot:
  def ping(self, src, type, dst, text):
    """Respond to ping"""
    self.irc.send('PONG :' + params["text"])
  def privmsg(self, src, type, dst, text):
    """Respond to ping"""
    self.irc.send('PRIVMSG chommik :bla')

  def __init__(self):
    self.irc = irc.Irc()
    self.irc.server = config['server']
    self.irc.port = config['port']
    self.irc.connect()
    self.irc.send('NICK ' + config['nick'])
    self.irc.send('USER ' + config['username'] + ' 0 * :' + config['realname'])

    self.binds = { 'PRIVMSG' : [ self.privmsg ] }

    while 1:
      cmd = self.irc.get().rstrip()
      print('>> ', str(cmd))
      args = cmd.split(' ')
      if args[0] == "PING":
        self.irc.send('PONG ' + args[1])
        continue
      (src,type,dst,text) = args[0][1:], args[1], args[2], ' '.join(args[3:])[1:]
      if type in self.binds:
        for func in self.binds[type]:
          _thread.start_new_thread(func, (src, type, dst, text))

  def bind(self,event,function):
    if event in self.binds:
      self.binds[event].insert(len(self.binds[event]),function)
    else:
      self.binds[event] = [ function ]
