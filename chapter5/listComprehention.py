#!/usr/bin/env python

#general syntax [ i for i in lst (if ....)]
#works in place of 2-D loops
#returns a list always

print [i for i in range(1,100)]

print [i for i in range(1,101) if (i%5)==0]

#2-D loops
#normal approach

for i in range(1,6):
	for j in range(1,6):
		print i,j  

#python approach
print [(i,j) for i in range(1,6) for j in range(1,6) ]

girls =['alice','bernice','clarice']
boys =['chris','arnold','bob']


result = [b+ '+' +g for b in boys for g in girls if b[0]==g[0]]
print type(result)
print result

#to get an enumeration object
result = list(enumerate([b+ '+' +g for b in boys for g in girls if b[0]==g[0]]))
print result
