#!/usr/bin/python
import sys
from scapy.all import *
try:
	if sys.argv[2] == "-all":
		host = str(sys.argv[1])
		for x in range(1,65536):
			port = int(x)
			pkt = sr1(IP(dst=host)/TCP(flags="S",dport=port), timeout=2, verbose=0)
			if pkt.sprintf("%TCP.flags%") == "SA":
				print "Port Open " + str(x)
	elif str(sys.argv[2]) == "-p" and sys.argv[3] is not "":
		port = int(sys.argv[3])
		host = str(sys.argv[1])
		pkt = sr1(IP(dst=host)/TCP(flags="S",dport=port), timeout=2, verbose=0)
		if pkt.sprintf("%TCP.flags%") == "SA":
			print "Port Open " + str(port)
	else:
		print "Usage : ./arpscanner.py <host> -all or -p [for specific port]"
except Exception as ex:
	print "Usage : ./arpscanner.py <host> -all or -p [for specific port]"
	print str(ex)
