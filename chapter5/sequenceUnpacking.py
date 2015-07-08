#!/usr/bin/env python

__author__ = 'Ovi'

#Simultaneous assignment is possible in python

x,y,z = 1,2,3

#swapping is very easy
x,y =y,x

print x,y,z

#this is sequence unpacking because it unpacks the sequence and assigns values to individual variables

temp = x,y,z
print temp

a,b,c = temp

print a,b,c

#useful when returning more than one value is necessary
def func():
    dic= { 'name':'ovi','age':24}
    return dic.popitem()

key,value = func()
print key,value


