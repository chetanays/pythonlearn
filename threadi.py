#!/usr/bin/env python
import threading
import Queue
import time

class workerclass(threading.Thread):
	def __init__(self,queue):
		threading.Thread.__init__(self)
		self.queue = queue
	
	def run(self):
		print "In worker thread"
		while True:
			count = self.queue.get()
			print "Sleeping %d second" % count
			time.sleep(count)
			print "Wake up after %d second" % count
			self.queue.task_done()

queue = Queue.Queue()

for i in range(10):
	wc = workerclass(queue)
	wc.setDaemon(True)
	wc.start()
	print "thread number 1 created %d " % i

for j in range(10):
	queue.put(j)

queue.join()

print "Finish task"

