#!/usr/bin/env python3
from boofuzz import *

RHOST = "192.168.0.108"
RPORT = 9999

session = Session(target=Target(connection=SocketConnection(RHOST,RPORT,proto="tcp")))

s_initialize("hter mode")
s_string("HTER", fuzzable=False)
s_delim(" ", fuzzable=False)
s_string("fuzz", fuzzable=True)

session.connect(s_get("hter mode"))
session.fuzz()
