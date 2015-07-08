#!/usr/bin/env python

#initializing a dictionary

d = {1:"hello",2:"Hi"}
print d, type(d)

#coverting a tuple into a dictionary 
#remember, a dictionary ha sno ordering 
items =[('name','Gumby'),('age',42)]
print dict(items), type(dict(items))

# converting argument into a dictionary
items = dict(name='Gumby', age = 42)
print items, type(items)
