#!/usr/bin/python
from scapy.all import *
ssidlist = []
while 1:
	pkt = sniff(iface='mon0',count=1)
	ssid = pkt[0].sprintf("%Dot11Elt.info%")
	if len(ssid) > 1 and "??" not in str(ssid) and "''" not in str(ssid):
		if str(ssid) not in ssidlist:
			ssidlist.append(str(ssid))
		elif str(ssid) in ssidlist:
			print str(ssid)
			
