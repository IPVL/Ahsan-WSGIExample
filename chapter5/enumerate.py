#!/usr/bin/env python

strings =['heloxxx','xxx','notxxx']
for index, string in enumerate(strings):
	if 'xxx' in string:
		strings[index] = '[censored]'

print strings
