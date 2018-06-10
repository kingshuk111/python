#!/usr/bin/python

import sys
print "starting python script"

file=open("experian","r")
#for line in file:
 #print line
print file.read()
file.close()
