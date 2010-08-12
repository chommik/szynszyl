from config import config

class BaseModule(object):
  def __init__(self):
    """BaseModule contructor"""
    self.config = Config()

  def is_priv(self, src):
    """Checks if sent command is private, or channel"""
    if src[0] == "#":
      return False
    else:
      return True
  def is_channel(self, src):
    """Checks if sent command is private, or channel"""
    if src[0] == "#":
      return True
    else:
      return False
  def is_admin(self,src):
    """Checks if user is admin"""
    if src in config['admins']:
      return True
    else:
      return False

