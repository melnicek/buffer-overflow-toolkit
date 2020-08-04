#!/usr/bin/env python3
from boofuzz import *

# Initialize RHOST(IP address) and RPORT(port).
RHOST = "192.168.0.109"
RPORT = 9999

# Create a session based on RHOST and RPORT.
s = Session(target=Target(connection=SocketConnection(RHOST,RPORT,proto="tcp")))

# Initialize fuzzer, name doens't matter.
s_initialize("FUZZER")

# Something like HTER, TRUN, etc.
s_string("comman", fuzzable=False)

# I need more research into difference between string and delim.
s_delim(" ", fuzzable=False)

# This parameter will be fuzzed.
s_string("this will be fuzzed")

# Connect fuzzer to your session.
s.connect(s_get("FUZZER"))

# Start your fuzzing.
s.fuzz()