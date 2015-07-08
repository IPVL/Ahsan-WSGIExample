#!/usr/bin/env python

lst = [1,2,3]

#added an element at the end, in place
lst.append(4)

print lst

print len(lst)

#find frequencies of an element
print lst.count(1)

#extend method looks like concatenation but original list changed

a= [1,2]
b= [3,4]

print "a=", a
print "b=", b

print "a+b= ", a+b, "a=",a ,"b=",b

print "a.extend(b)= ", a.extend(b), "a=",a, "b=",b

#return index of the element if exists
print a.index(4)

#insert adds an element to an a specific index
b.insert(2,4)
print b

#The pop method is the only list method that both modifies the list and returns a value

print a.pop()

print a.pop(0)

#to reverse the list
lst.reverse()
print lst

#reversed is a function and return an iterator
x= [1,2,3,4]
print reversed(x)
print list(reversed(x))

