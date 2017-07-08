#!/usr/bin/env python3
#-*- coding:utf-8 -*-
class myclass(object):
	def __str__(self):
		return "this is Myclass"
	def __init__(self,name="wangxw"):
		self.name=name
	def outinfor(self):
		print("my name is:%s"%self.name)	

s=myclass()
print(s)
print(myclass())
s.outinfor()