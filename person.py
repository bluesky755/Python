#/usr/bin/env python
# -*- coding: utf-8 -*-
'This is the first class I ever created using python '
class Person:
	def __init__(self,name,age):
		self.name=name
		self.age=age
	def printinfor(self):
		print("name1:%s,age1:%d" %(self.name,self.age))
	def __len__(self):
		return 100