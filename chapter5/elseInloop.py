#!/usr/bin/env python

from math import sqrt 

# here the else clause is executed as break is not called

for i in range(99,81,-1):
	val = sqrt(i)
        if val == int(val):
		print "got it"
		break;
else:
	print "I didn't get it!"
