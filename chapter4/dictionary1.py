#!/usr/bin/env python


people = {
	'Alice': {
		'phone': '2341',
		'addr': 'Foo drive 23'
		 },

    	'Beth': {
		'phone': '9102',
		'addr': 'Bar street 42'
		},

	'Cecil': {
		'phone': '3158',
		'addr': 'Baz avenue 90'
		 }
	}

labels = {
	'phone': 'phone number',
	'addr': 'address'
	}

name = raw_input("Enter a name:")
lebel = raw_input("Enter a lebel:(p) or (a)")

if lebel=="p":
	key = 'phone'
elif lebel=="a":
	key = 'addr'
else:
	print "Try again"


if name in people:
	print "%s's %s is %s"% (name,key,people[name][key]) 
