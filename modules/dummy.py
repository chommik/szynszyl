class Module:
  def __init__(self,bot):
    self.bot = bot
    print("woohoo")
    self.bot.bind('376',self.onconnect)

  def onconnect(self, src, type, dst, text):
    #: TODO
    print('ciamciaciamcia')