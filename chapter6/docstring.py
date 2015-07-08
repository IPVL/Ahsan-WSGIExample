#!/usr/bin/env python

def demofunc(x):
	'This function is created for docstring demonstration.'
	print 'This is the function body',x

print demofunc.__doc__
demofunc(1)

print help(demofunc)
