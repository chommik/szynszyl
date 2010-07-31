# -*- encoding: utf-8 -*-
import dns
import dns.resolver
from log import log

class Module:
  def __init__(self, bot):
    """Module constructor"""
    self.bot = bot
    self.irc = bot.irc
    self.bot.bind('PRIVMSG', self.dns)

  def dns(self, src, type, dst, text):
    if dst[0] != '#' or text[0] != '.':
      return
    args = text.split(' ')
    if args[0] == ".dns":
      self.query(src, type, dst, text)
    elif args[0] == ".ptr":
      self.ptr(src,type,dst,text)

  def query(self, src, type, dst, text):
    """PRIVMSG handler
      syntax: .dns <query> <type>
              .dns <query>
    """
    allowedtypes = ['A','AAAA','SOA','MX','TXT','SRV','PTR']
    args = text.split(' ')

    if len(args) == 3:
      query = args[1]
      type = args[2]
      if not type in allowedtypes:
        self.irc.send('PRIVMSG {dst} :{src}: Niepoprawna składnia. (1)'.format(src=src,dst=dst))
        return
    elif len(args) == 2:
      query = args[1]
      type = 'A'
    else:
      self.irc.send('PRIVMSG {dst} :{src}: Niepoprawna składnia. (0)'.format(src=src,dst=dst))
      return
    answers = dns.resolver.query(query, type)
    ans = ""
    for answ in answers:
      ans += str(answ) + " "
    self.irc.send('PRIVMSG {dst} :{query}. IN {typ} {ans}'.format(dst=dst,query=query,typ=type,ans=ans))