#!/usr/bin/env python

#find() method finds a substring from a larger strings and reurn its starting index 
print 'With a moo-moo here, and a moo-moo there'.find('moo')

#if not found, return -1

print 'Hello, World!'.find('ovi') 


subject = '$$$ Get rich now!!! $$$'
print subject.find('$$$')

# supplying the start for finding
print subject.find('$$$', 1) 
subject.find('!!!')

# Supplying start and end
print subject.find('!!!', 0, 16) 

#join() works like the inverse of split()
lst =['Welcome','to','Bangladesh']
lst_joined = ' '.join(lst)
print lst_joined

dirs = '', 'usr', 'bin', 'env'

add = '/'.join(dirs)
print add

#lower() method makes a string all-lower case

demo ="ThiS Is a CaMel cAsed StrIng"
print demo.lower() 

#replace() replaces a substring with another substring()

print "This is a test".replace('is','eez')

#split() is used to split a string into several substring

demo ="ThiS Is a CaMel cAsed StrIng"
print demo.split()

#strip() strips white spaces and other values
print '*** SPAM * for * everyone!!! ***'.strip(' *!')

