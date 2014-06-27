#!/usr/bin/env python
import socket
import binascii
import struct
import time

TCP, IP, HTTP = False, False, False
class bf(object):
    def __init__(self,value=0):
        self._d = value

    def __getitem__(self, index):
        return (self._d >> index) & 1

    def __setitem__(self,index,value):
        value    = (value&1L)<<index
        mask     = (1L)<<index
        self._d  = (self._d & ~mask) | value

    def __getslice__(self, start, end):
        mask = 2L**(end - start) -1
        return (self._d >> start) & mask

    def __setslice__(self, start, end, value):
        mask = 2L**(end - start) -1
        value = (value & mask) << start
        mask = mask << start
        self._d = (self._d & ~mask) | value
        return (self._d >> start) & mask

    def __int__(self):
        return self._d

def ETHparse(ethh):
	global IP
	(ethd, eths, etht) = struct.unpack("!6s6s2s", ethh)
	print "Recieving Data from"
	print "Destination MAC - " + str(binascii.hexlify(ethd))
	print "Source MAC - " + str(binascii.hexlify(eths))
	if binascii.hexlify(etht) == '0800':
		IP = True
 
def IPparse(iph):
	ipdata = struct.unpack("!9s1s2s4s4s", iph)
	global TCP
	print "Destination IP - " + socket.inet_ntoa(ipdata[3])
	print "Source IP - " + socket.inet_ntoa(ipdata[4])
	if binascii.hexlify(ipdata[1]) == '06':
		TCP = True

def TCPparse(tcph):
	ofs = bf()
	global HTTP
	(sp, dp, seq, ack, ofs[0:16], win, cs, up) = struct.unpack("!HHLLHHHH", tcph)
	print "Source port %d" % sp
	print "Destinition port %d" % dp
	print "Sequence number %d" % seq
	print "Acknowledgement number %d" % ack
	print "Data offset ",int(ofs[0:4])
	print "URG %d" % ofs[10]
	print "ACK %d" % ofs[11]
	print "PSH %d" % ofs[12]
	print "RST %d" % ofs[13]
	print "SYN %d" % ofs[14]
	print "FIN %d" % ofs[15]
	print "Window Size %s" % str(win)
	print "Check sum %s" % str(cs)
	print "Urgent pointer %s" % str(up)
	if (sp == 80) or (dp == 80):
		HTTP = True

def HTTPparse(httph):
	print "Data " + httph
	time.sleep(3)

sock = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))
while 1:
	pkt = sock.recvfrom(2048)
	TCP, IP, HTTP = False, False, False
	ETHparse(pkt[0][0:14])
	if IP:
		IPparse(pkt[0][14:34])
	if TCP:
		TCPparse(pkt[0][34:54])
	if HTTP:
		HTTPparse(pkt[0][54:])
	print "--------------------------------"
