#!/usr/bin/env python

from string import Template

s = Template('$x, mighty $x!')
print type(s)

print s.substitute( x= "Tiger")
#print s

#A dictionary can be pass to substitute a template

s = Template("He is $x but $y")
virtue ={'x':'poor', 'y':'honest'}

print s.substitute(virtue)
