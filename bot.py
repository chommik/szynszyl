# -*- encoding: utf-8 -*-

import irc
from config import *
import thread
from log import log
from time import sleep
import imp
import sys
import thread

class Bot:
  def __init__(self):
    self.irc = irc.Irc()
    self.irc.server = config['irc']['server']
    self.irc.port = config['irc']['port']
    self.irc.connect()
    self.irc.send('NICK ' + config['irc']['nick'])
    self.irc.send('USER ' + config['irc']['username'] + ' 0 * :' + config['irc']['realname'])

    self.loadmodules()

    tries = 0
  
    while 1:
      cmd = self.irc.get()
      if cmd == None:
        log('Disconnected from server', 'ERROR')
        if tries > config['irc']['reconnect']['maxtries']:
          log('Maximum number of tries reached. Quitting.','CRIT')
          break
        if config['irc']['reconnect']['allow'] == 0:
          log('Reconnecting disallowed. Quitting.','CRIT')
          break
        elif config['irc']['reconnect']['allow'] == 1:
          sleep(config['irc']['reconnect']['timeout'])
          log('Trying to reconnect.')
          self.irc.connect()
          tries += 1
          continue
      cmd = cmd.rstrip()
      log(str(cmd),'DEBUG')
      args = cmd.split(' ')
      if args[0] == "PING":
        self.irc.send('PONG ' + args[1])
        continue
      elif args[0] == "ERROR":
        log('ERROR: ' + ' '.join(args[1:]),'ERROR')
      (src,type,dst,text) = args[0][1:], args[1], args[2], ' '.join(args[3:])[1:]
      if type in self.binds:
        for func in self.binds[type]:
          thread.start_new_thread(func, (src, type, dst, text))

  def bind(self,event,function):
    if not event in self.binds:
      self.binds[event] = [ ]

    self.binds[event].insert(len(self.binds[event]),function)
    log('Bindtable was updated. Bindtable now: ' + repr(self.binds), 'DEBUG')

  def loadmodules(self):
    """Loads modules"""
    self.binds = {}
    for mod in config['modules']['_autoload']:
      log('loading module ' + mod)
      __import__('modules.' + mod)
      sys.modules['modules.' + mod].Module(self)
      
  def reloadmodules(self):
    """Reloads modules"""
    imp.reload(sys.modules['config'])
    for mod in config['modules']['_autoload']:
      imp.reload(sys.modules['modules.' + mod])
    self.loadmodules()

  def shutdown(self):
    """Closes IRC connection and turns off the bot"""
    self.irc.disconnect()