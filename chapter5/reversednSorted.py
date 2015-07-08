#!/usr/bin/env python

lst =[1,2,3,4,5]

# Sorted returns a list
sorted(lst)
print lst

print sorted("Hello World!")

#Reversed returns a mistrious iterable object so need to cast into list

print list(reversed("Hello world"))

#join method can be used to join with String

print ''.join(reversed("Hello World!"))
