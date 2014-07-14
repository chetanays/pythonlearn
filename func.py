#!/usr/bin/python
import socket
def retBanner(ip, port):
	try:
		socket.setdefaulttimeout(2)
		s = socket.socket()
		s.connect((ip, port))
		banner = s.recv(1024)
		return str(banner)
	except Exception as ex:
		return str(ex)
def checkvuln(banner):
	if "Microsoft" in str(banner):
		print str(banner) + " is Vulnerable"
	elif "Linux" in str(banner):
		print str(banner) + " is protected"
def main():
	ip1 = '192.168.1.130'
	ip2 = '192.168.1.131'
	port = 21
	banner1 = retBanner(ip1,port)
	if banner1:
		print '[+] ' + ip1 + ': ' + banner1
		checkvuln(str(banner1))
	banner2 = retBanner(ip2,port)
	if banner2:
		print '[+] ' + ip2 + ': ' + banner2
		checkvuln(str(banner2))
if __name__ == '__main__':
	main()
