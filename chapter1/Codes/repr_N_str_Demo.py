#!/usr/bin/env python

# repr & str both convert values to string when print

#use of repr, converts to a string that is a representation of value as legal python expression

print repr("Hello, world!")
print repr(10000L)

#use of str, converts to a string simply regardless of being legal python expression

print str("Hello, world!") 
print str(10000L)
