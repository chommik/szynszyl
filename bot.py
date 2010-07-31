# -*- encoding: utf-8 -*-

import irc
from config import *
import thread
from log import log
import imp
import sys
import thread

class Bot:
  def __init__(self):
    self.irc = irc.Irc()
    self.irc.server = config['server']
    self.irc.port = config['port']
    self.irc.connect()
    self.irc.send('NICK ' + config['nick'])
    self.irc.send('USER ' + config['username'] + ' 0 * :' + config['realname'])

    self.loadmodules()

    while 1:
      cmd = self.irc.get().rstrip()
      if not cmd:
        break
      log(str(cmd),'DEBUG')
      args = cmd.split(' ')
      if args[0] == "PING":
        self.irc.send('PONG ' + args[1])
        continue
      elif args[0] == "ERROR":
        log('ERROR: ' + ' '.join(args[1:]),'ERR')
      (src,type,dst,text) = args[0][1:], args[1], args[2], ' '.join(args[3:])[1:]
      if type in self.binds:
        for func in self.binds[type]:
          thread.start_new_thread(func, (src, type, dst, text))

  def bind(self,event,function):
    if not event in self.binds:
      self.binds[event] = [ ]

    self.binds[event].insert(len(self.binds[event]),function)
    log('bindtable now: ' + repr(self.binds))

  def loadmodules(self):
    """Loads modules"""
    self.binds = {}
    for mod in config['loadmodules']:
      log('loading module ' + mod)
      __import__('modules.' + mod)
      sys.modules['modules.' + mod].Module(self)
  def reloadmodules(self):
    """Reloads modules"""
    imp.reload(sys.modules['config'])
    for mod in config['loadmodules']:
      imp.reload(sys.modules['modules.' + mod])
    self.loadmodules()

  def shutdown(self):
    """Closes IRC connection and turns off the bot"""
    self.irc.disconnect()