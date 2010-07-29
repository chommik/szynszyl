import irc
from config import *

class Bot:
  def __init__(self):
    self.irc = irc.Irc()
    self.irc.server = config['server']
    self.irc.port = config['port']
    self.irc.connect()
