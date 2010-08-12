# -*- encoding: utf-8 -*-

from config import config
from time import strftime

flog = open(config['bot']['log']['file'], 'w')

def log(text, type='INFO'):
  """Logs data"""
  if type ==  'INFO':
    prefix = '>>'
  elif type == 'ERROR':
    prefix = '!!'
  elif type == 'CRIT':
    prefix = '##'
  elif type == 'DEBUG':
    if config['bot']['debugmode'] == 0:
      return
    prefix = '--'
  else:
      prefix = 'FIXME_WRONG_CODE'

  date = strftime(config['bot']['log']['dateformat'])
  flog.write(config['bot']['log']['logformat'].format(prefix=prefix, date=date, text=text) + "\n")
  flog.flush()