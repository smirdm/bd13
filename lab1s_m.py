#!/usr/bin/python
#!/bin/python 
import sys

for line in sys.stdin:
	
	u1, u2, country, u3, payout = line.strip().split(',')
	print '\t'.join([country.strip(), payout.strip()])
