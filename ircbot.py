#!/usr/bin/python
# -*- encoding: utf-8 -*-

from bot import Bot
from config import config
from log import log

def daemonize():
  try:
    pid = os.fork()
    if pid > 0:
        sys.exit(0)
  except OSError as e:
    log("fork #1 failed: {0} ({1})\n".format(e.errno, e.strerror),'CRIT')
    sys.exit(1)
    os.chdir("/")
    os.setsid()
    os.umask(0)
    try:
      pid = os.fork()
      if pid > 0:
        sys.exit(0)
    except OSError as e:
      log('CRITICAL',"fork #2 failed: {0} ({1})\n".format(e.errno, e.strerror),'CRIT')
      sys.exit(1)

if __name__ == "__main__":
  if config['background']:
    daemonize()
  log('szynszyl starting...')
  bot = Bot()
  