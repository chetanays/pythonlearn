#!/usr/bin/python
import nmap
import optparse
import threading
scrnLock = threading.Semaphore(value=1)
def nmapScan(tgtHost, tgtPort):
	nmScan = nmap.PortScanner()
	try:
		nmScan.scan(tgtHost, tgtPort)
		state = nmScan[tgtHost]['tcp'][int(tgtPort)]['state']
		scrnLock.acquire()
		print "[*] " + tgtHost + " tcp/" + tgtPort + " " + state
	except:
		pass
	finally:
		scrnLock.release()
		
def main():
	parser = optparse.OptionParser('Usage %prog -H <target host> -p <target ports>')
	parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
	parser.add_option('-p', dest='tgtPort', type='string', help='specify target ports seperated by comma')
	(option, args) = parser.parse_args()
	tgtHost = option.tgtHost
	tgtPorts = str(option.tgtPort).split(',')
	if (tgtHost == None) | (tgtPorts[0] == None):
		print parser.usage
		exit(0)
	for tgtPort in tgtPorts:
		t = threading.Thread(target=nmapScan, args=(tgtHost, tgtPort))
		t.start()
		#nmapScan(tgtHost, tgtPort)
if __name__ == '__main__':
	main()
