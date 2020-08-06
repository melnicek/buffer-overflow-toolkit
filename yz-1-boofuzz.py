#!/usr/bin/env python3
from boofuzz import *

RHOST = "192.168.0.109"
RPORT = 9999

s = Session(target=Target(connection=SocketConnection(RHOST,RPORT,proto="tcp")))

s_initialize("FUZZER")
s_string("example", fuzzable=False)
s_delim(" ", fuzzable=False)
s_string("fuzz")

s.connect(s_get("FUZZER"))
s.fuzz()