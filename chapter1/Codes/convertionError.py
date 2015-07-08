#!/usr/bin/env python

#invalid, TypeError: cannot concatenate 'str' and 'int' objects
temp =40
print "temp =" + temp

# valid
print "temp =" + repr(temp)
print "temp =" + `temp`
