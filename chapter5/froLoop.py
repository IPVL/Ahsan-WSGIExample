#!/usr/bin/env python
__author__ = 'Ovi'

var = range(1,10)
print var

var = range (10)
print var

var = range(0)
print var

var = range(9,10)
print var

for i in range(1,101):
    print i,
print "\n"

for i in range(1,101,2):
    print i,
print "\n"
#iterating over a dictionary

demo ={1:'sat',2:'sun',3:'mon'}
for key in demo:
    print key, demo[key]

#sequence unpacking can be used

for key,value in demo.items():
    print key,value
