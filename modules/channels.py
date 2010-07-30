from config import config

class Module:
  def __init__(self,bot):
    self.bot = bot
    self.bot.bind('376',self.onconnect)

  def onconnect(self, src, type, dst, text):
    for chan in config['joinchannels']:
      self.bot.irc.send('JOIN ' + chan)