#!/usr/bin/env python
from scapy.all import *

conf.L3socket
conf.L3socket=L3RawSocket

ip = IP()
t = TCP()

ip.dst = 'packtpub.samsclass.info'
t.dport = 40001

response = sr1(ip/t)

t.flags = "A"
t.seq = response.ack
t.ack = response.seq + 1

send(ip/t/"V413H4V")

