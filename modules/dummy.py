from modules import BaseModule
from config import config

class Module(BaseModule):
  def __init__(self,bot):
    self.config = BaseModule.Config(self.__class__.__name__)
    self.bot = bot

  def privmsg(self, src, type, dst, text):
    #: PRIVMSG handler
    pass