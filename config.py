# -*- encoding: utf-8 -*-

import sys

config = {}

config['name'] = 'ircbot'
config['server'] = '::1'
config['port'] = 6667

config['nick'] = 'szynszyl'
config['username'] = 'bot'
config['realname'] = 'Bot'

config ['loadmodules'] = ['channels', 'link', 'commands', 'ctcp', 'dnsclient']

config['background'] = 1

config['log'] = sys.stderr
#inna możliwość:
#config['log'] = open('szynszyl.log','w')
config['logformat'] = '{date} {prefix} {text}'
config['dateformat'] = "%Y-%m-%d %H:%M:%S"

config['debugmode'] = 0

config['joinchannels'] = ['#bot','#pz','#main']

config['admins'] = [ 'chommik!rafal@staff.netadmin' ]
