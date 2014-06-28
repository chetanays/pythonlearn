#!/usr/bin/python
import threading
import Queue
import sys
from scapy.all import *
class workerclass(threading.Thread):
	def __init__(self, queue, host):
		threading.Thread.__init__(self)
		self.queue = queue
		self.host = host

	def run(self):
		port = 1
		while port < 1000:
			port = int(self.queue.get())
			print "working on port %d " % port
			pkt = sr1(IP(dst=str(self.host))/TCP(flags="S",dport=int(port)),timeout=1,verbose=0)
			if pkt.sprintf("%TCP.flags%") == "SA":
				print "Port Open " + str(x)	
		self.queue.task_done()
		sys.exit(0)

try:
	queue = Queue.Queue()
	host = sys.argv[1]
	for x in range(1,10):
		wc = workerclass(queue,host)
		wc.setDaemon(True)
		wc.start()

	for y in range(1,1000):
		queue.put(y)
	queue.join()
except Exception as ex:
	print str(ex)
	print "Usage ./synthread.py <ip>"

	
