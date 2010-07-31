# -*- encoding: utf-8 -*-

import sys

config = {}

config['name'] = 'ircbot'
config['server'] = '::ffff:192.168.2.54'
config['port'] = 6667

config['nick'] = 'py-szynszyl'
config['username'] = 'bot'
config['realname'] = 'Bot'

config ['loadmodules'] = ['channels', 'link', 'commands', 'ctcp', 'dnsclient']

config['background'] = 0

config['log'] = sys.stderr
#inna możliwość:
#config['log'] = open('szynszyl.log','w')
config['logformat'] = '{date} {prefix} {text}'
config['dateformat'] = "%Y-%m-%d %H:%M:%S"

config['debugmode'] = 1

config['joinchannels'] = ['#bot']

config['admins'] = [ 'chommik!rafal@staff.netadmin' ]