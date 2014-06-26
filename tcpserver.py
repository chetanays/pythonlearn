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

sock = SocketServer.TCPServer(addr, Echohandler)
sock.serve_forever()
