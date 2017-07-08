#!/usr/bin/env python
def log1(func):
	def wrapper(*args,**dict1):
		print("your are calling %s" %func.__name__)
		return func(*args,**dict1)
	return wrapper
@log1
def testfunc():
	print("This is a function used for test!")

testfunc()
