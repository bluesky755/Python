#!/usr/bin/env python3
#--*- coding:utf-8 -*-
from types import MethodType
class Animal(object):

	__type=""
	def __init__(self):
		__type="None"
	def running(self):
		print("%s is running!"%self.__type)

class Bird(object):
	__type=""
	def __init__(self):
		pass
		self.__type="bird"
	def flying(self):
		print("%s is flying" %self.__type)

class dog(Animal):
	__slots__=('name','type')
	def __init__(self):
		self.__type="dog"
		self.__legs=4
	def running(self):
		print("%s is running" % self.__type)

s=dog()
s.running()

def KillMan(self,name):
	print("You will kill man %s" % name)

s.KillMan=MethodType(KillMan,s)
s.KillMan("one")
s.name="test"
s.age=10
print("Age is %d" %s.age)