#!/usr/bin/env python


#passing a tuple as conversion specifiers 
format = "hi %s, are you %s ?"
value1 = ('ovi','ok')
value2 = ('ahsan','mad')
print format % value1
print format % value2

#for precision, use dot and a number before conversion specifier

from math import pi as p
format = "Value of Pi is %.3f"
print format%p 
