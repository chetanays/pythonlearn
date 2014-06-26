#!/usr/bin/python
import threading
import Queue
import ftplib
import re
class workingclass(threading.Thread):
	def __init__(self,queue,lock):
		threading.Thread.__init__(self)
		self.queue = queue
		self.lock = lock

	def run(self):
		while True:
			dirlist = []
			link = self.queue.get()
			print "Fetching dirctory list from %s " % link
			try:
				ftp = ftplib.FTP(link)
				ftp.login()
				ftp.retrlines('LIST', dirlist.append)
				ftp.close()
			except Exception as exc:
				print " "		
			self.lock.acquire()
			file = open('ftpscan.txt','a')
			file.write('Site %s \n' % link)
			for li in dirlist:
				file.write(li + '\n')
			file.write('\n')
			file.close()
			self.lock.release()
			self.queue.task_done()

queue = Queue.Queue()
lock = threading.Lock()
urlist = []
file = open("ftplist.txt","r")
for url in file.readlines():
	match = re.search(r'/([\w.]+)',url)
	if match:
		if match.group(1) in url:
			urlist.append(match.group(1))
file.close()
for i in range(5):
	wc = workingclass(queue,lock)
	wc.setDaemon(True)
	wc.start()

for x in urlist:
	queue.put(x)

queue.join()		

print "Mission Success"	
