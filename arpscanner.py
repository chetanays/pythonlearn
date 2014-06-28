#!/usr/bin/python
from scapy.all import *

for x in range(1,256):
	ip = "192.168.1." + str(x)
	pkt = Ether(dst="FF:FF:FF:FF:FF:FF")/ARP(pdst=ip,hwdst="FF:FF:FF:FF:FF:FF")
	rep = srp1(pkt,verbose=0,timeout=1)
	if rep:
		print "IP Found " + rep.psrc + " MAC Address " + rep.hwsrc 
