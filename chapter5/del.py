#!/usr/bin/env python

# del deletes the name, not the value. Python's garbage collection does that
 
x = ["Hello","world"]
y =x

del x
print y
