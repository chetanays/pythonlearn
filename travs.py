#!/usr/bin/python

import sys, os

sta = raw_input("Enter the initial directory")
for dirname, subdir, filename in os.walk(sta):
	print " [+]-- %s" % dirname
	for fname in filename:
		print "[+]- %s" % fname
 
