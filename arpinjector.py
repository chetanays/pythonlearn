#!/usr/bin/python

import struct
import socket

sock = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))
sock.bind(("eth1",socket.htons(0x0800)))
try:
	packt = struct.pack("!6s6s2s2s2s1s1s2s6s4s6s4s","\xff\xff\xff\xff\xff\xff","\xbb\xbb\xbb\xbb\xbb\xbb","\x08\x06","\x00\x01","\x08\x00","\x06","\x04","\x00\x01","\xbb\xbb\xbb\xbb\xbb\xbb","\xff\xff\xff\xff","\x00\x00\x00\x00\x00\x00","\xff\xff\xff\xff")
except Exception as excep:
	print excep
sock.send(packt)
sock.close()
