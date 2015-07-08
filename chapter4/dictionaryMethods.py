#!/usr/bin/env python

#clear method

x={}
y = x

x['key']= 'value'

print y


x.clear()

print y

#copy method

from copy import deepcopy
d = {}
d['names'] = ['Alfred', 'Bertrand']
c = d.copy()
dc = deepcopy(d)
d['names'].append('Clive')
print c

print dc

#fromKeys method

print dict.fromkeys(['name','age','address'])
  #change default value

print dict.fromkeys(['name','age'],'unknown')

#get method helps to avoid some error like no item exception

a={}
#print a['name'] will give an error
print a.get('name') # we output 'None'
print a.get('name','def_value') #We output "def_value"

#items method returns a list whereas iteritems methods returns an iterable
d={'name':'Kan','roll':1, 'home':'Rangpur'}
print d.items(), type(d.items())
print list(d.iteritems()), type(d.iteritems())

#keys and iterkeys returns a list and iterable of keys respectively
print d.keys(),type(d.keys())


#pop() returns a value by a key and deletes it from the sequence
lst= {'x':1,'y':2,'z':3}
print lst.pop('x'), lst

#popitem() returns an arbitary item from the sequence
a,b =lst.popitem()

print a,b


#setdefault() tries to fetch an item and if not exist set a default value and add it to the sequence 
print lst.setdefault('a','Unknown')
print lst

print lst.setdefault('a','known')
