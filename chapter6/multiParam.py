#!/usr/bin/env python

# '*' used to take an arbitary  number of parameter
#stored and bind as a tuple 
def print_param(*params):
	print params


print_param("a","b","c")


def print_param(par,*params):
	print par, params


print_param("good","a","b","c")

# '**' used to store keyward argument. returns a dictionary rather than a tuple

def print_param2(**params):
	print params

print_param2(x=2, y=3,z=4)


def print_param3(x,y,z=3,*param,**param2):
	print x,y,z
	print param
	print param2


print_param3(1,2,3,4,5,6,7,foo=9,bar=10)

def add(*params):
	print params[0]


add(1,2,3)

