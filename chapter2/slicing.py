#!/usr/bin/env python

numbers = [1,2,3,4,5,6,7,8,9,10]

#start inclusive, end exclusive



#outputs [1,2,3,4]
print numbers[0:4]  

#outputs [8,9,10]
print numbers[7:10] 


#outputs [8,9]
print numbers[7:-1]

#outputs [8,9,10]
print numbers[7:]

#outputs [1,2,3] 
print numbers[:3]

#outputs [1,2,3,4,5,6,7,8,9,10]
print numbers[:]

#outputs [1,3,5,7,9]
print numbers[::2]

#outputs []
print numbers[2:8:-1]

#outputs [9,7,5]
print numbers[8:2:-2]
