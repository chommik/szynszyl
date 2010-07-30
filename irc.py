# -*- encoding: utf-8 -*-

from config import *
import socket

class Irc:
  #TODO: dodać obsługę błędów
  server = ''
  port = 0
  opened = 0

  def __init__(self):
    """Init socket and connection"""
  def send(self,text):
      """Send data to server"""
  def connect(self):
    """Open IRC socket"""
    self.sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    self.sock.connect((self.server, self.port))
    self.fsock = self.sock.makefile()
    self.opened = 1
    return 0
  def disconnect(self):
    self.sock.close()
    self.opened = 0
    return 0
    """Close IRC socket"""
  def get(self):
    """Base loop"""
    data = self.fsock.readline()
    return data
  def send(self, text):
    """Send data to socket"""
    if self.opened:
      print('<< ', text)
      self.sock.send(text.encode()+b'\n')
