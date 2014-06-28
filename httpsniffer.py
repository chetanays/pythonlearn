#!/usr/bin/python
from scapy.all import *
import time
def sniffx(pktx):
	headerx = pktx.sprintf("%Raw.load%")
	print pktx.summary()
	if headerx.startswith("'GET") or headerx.startswith("'POST"):
		Httphead = headerx.split("\\r\\n")
		for x in Httphead:
			print x
	elif headerx.startswith("'HTTP"):
		Httphead = headerx.split("\\r\\n")
		for x in Httphead:
			print x

count = 0
pkt = sniff(filter="tcp port 80",count=30)
while count < 30:
	sniffx(pkt[count])
	count+=1
	print "--------------------------------"
