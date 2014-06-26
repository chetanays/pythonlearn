#!/usr/bin/env python
import SocketServer

class Echohandler(SocketServer.BaseRequestHandler):
	def handle(self):
		data = "dummy"
		while len(data):
			data = self.request.recv(2048)
			print "Data received " + data
			self.request.send(data)
			
		print "Client left"

addr = ("0.0.0.0", 9001)
class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass

server = ThreadedTCPServer(addr, Echohandler)
server.serve_forever()
