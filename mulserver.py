#!/usr/bin/python
import socket
import threading
import Queue

class workerclass(threading.Thread):
	def __init__(self, queue):
		threading.Thread.__init__(self)
		self.queue = queue

	def run(self):
		while True:
			portx = self.queue.get()
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
			sock.bind(("0.0.0.0",int(portx)))
			sock.listen(1)
			(client,(ip, port)) = sock.accept()
			data = "test"
			while len(data):
				data = client.recv(2048)
				print "Data recieved %s from port %s" % (data,portx)
				client.send(data)
			client.close()
			sock.close()


queue = Queue.Queue()
portlist = ['8000','8001','8002','8003','8004']

for i in range(5):
	wc = workerclass(queue)
	wc.setDaemon(True)
	wc.start()

for ix in portlist:
	queue.put(ix)

queue.join()
