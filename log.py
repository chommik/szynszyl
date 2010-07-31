# -*- encoding: utf-8 -*-

from config import config
from time import strftime

def log(text, type='INFO'):
  """Logs data"""
  if type ==  'INFO':
    prefix = '>>'
  elif type == 'ERROR':
    prefix = '!!'
  elif type == 'CRIT':
    prefix = '##'
  elif type == 'DEBUG':
    if not config['debugmode']:
      return
    prefix = '--'

  date = strftime(config['dateformat'])
  config['log'].write(config['logformat'].format(prefix=prefix, date=date, text=text) + "\n")
  config['log'].flush()