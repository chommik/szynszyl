from config import *
import socket

class Irc:
  server = ''
  port = 0

  def __init__(self):
    """Init socket and connection"""
  def bind(self,cmd,function):
    """Bind server event to function"""
  def send(self,text):
      """Send data to server"""
  def connect(self):
    """Open IRC socket"""
    self.sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    self.sock.connect((self.server, self.port))
    data = self.sock.recv(1024)
    print('Received', repr(data))
  def disconnect(self):
    self.sock.close()
    """Close IRC socket"""