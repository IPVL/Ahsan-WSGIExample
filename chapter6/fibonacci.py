#!/usr/bin/env python

def fibo(n):
	fibo_lst =[0,1]
	for i in range(n-2):
		fibo_lst.append(fibo_lst[-2]+fibo_lst[-1])
	return fibo_lst

print fibo(10) 
