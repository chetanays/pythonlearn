#!/usr/bin/python
import optparse
import socket
from threading import *
scrnLock = Semaphore(value=1)
def connScan(tgtHost, tgtPort):
	try:
		connSkt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		connSkt.connect((tgtHost, tgtPort))
		connSkt.send("Hello\r\n")
		ba = connSkt.recv(2048)
		scrnLock.acquire()
		print "[+] %d port open" % tgtPort
		print str(ba)
	except:
		scrnLock.acquire()
		print "[+] %d port closed" % tgtPort
	finally:
		scrnLock.release()
		connSkt.close()

def portScan(tgtHost, tgtPorts):
	try:
		tgtIP = socket.gethostbyname(tgtHost)
	except:
		print "[-] Cannot resolve %s : Unknown Host" % tgtHost
		return
	try:
		tgtName = socket.gethostbyaddr(tgtIP)
		print '\n[+] Scan Results for: ' + tgtName[0]
	except:
		print '\n[+] Scan Results for: ' + tgtIP
	socket.setdefaulttimeout(1)
	for tgtPort in tgtPorts:
		t = Thread(target=connScan, args=(tgtHost, int(tgtPort)))
		t.start()
		#print 'Scanning port ' + tgtPort
		#connScan(tgtHost, int(tgtPort))
		

def main():
	parser = optparse.OptionParser("Usage -H <target host> -p <target port>")
	parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
	parser.add_option('-p', dest='tgtPort', type='string', help='specify target port[s] sperated by comma')
	(option, args) = parser.parse_args()
	tgtHost = option.tgtHost
	tgtPorts = str(option.tgtPort).split(',')
	if (tgtHost == None) | (tgtPorts[0] == None):
		print parser.usage
		exit(0)
	portScan(tgtHost, tgtPorts)

if __name__ == '__main__':
	main()
