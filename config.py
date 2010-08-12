# -*- encoding: utf-8 -*-

import yaml

class Config:
  def __getitem__(self, item):
    """Gets config item"""
    if item in self.config:
      return self.config[item]
    else:
      raise KeyError

  def __setitem__(self, item, val):
    """Sets config item"""
    self.config[item] = c

  def __init__(self):
    """Inits config object"""
    self.load_config()


  def reload(self):
    """Reloads config ignoreing current values"""
    load_config(self)


  def load_config(self):
    f = open('config.yml','r')
    self.config = yaml.load(f)
    f.close()

  def save(self):
    """Saves config to file"""
    f = open('config.yml','w+')
    f.write = yaml.dump(self.config, explicit_start=True, default_flow_style=False)
    f.close()

config = Config()