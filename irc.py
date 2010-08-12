# -*- encoding: utf-8 -*-

from config import *
import socket
from log import log

class Irc:
  #TODO: dodać obsługę błędów
  server = ''
  port = 0
  opened = 0
  def connect(self):
    """Open IRC socket"""
    try:
      self.sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
      self.sock.connect((self.server, self.port))
      self.fsock = self.sock.makefile()
    except IOError as e:
      log('Cannot open socket, error: ' + str(e), 'ERROR')
    else:
      self.opened = 1
    return 0
  def disconnect(self):
    """Close IRC socket"""
    if self.opened:
      self.sock.close()
      self.opened = 0
      return 0
    else:
      return 1
  def get(self):
    """Wait for data from server and return it"""
    if self.opened:
      data = self.fsock.readline()
      return data
    else:
      return None
  def send(self, text):
    """Send data to socket"""
    if self.opened:
      log('<< ' + text, 'DEBUG')
      self.sock.send(text + '\n')
      return 0
    else:
      return 1
