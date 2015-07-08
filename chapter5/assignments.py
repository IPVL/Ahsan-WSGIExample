#!usr/bin/env python
__author__ = 'Ovi'

#chained assignments
x=y=2
print x,y

#Augmented assignments, they works even with strings
x="foo"
y="bar"
x+=y
print x

num =int(raw_input("Input:"))
if 1<=num<=10:
    print 'ok'
else:
    print not 'ok'
