#!/usr/bin/env python3
#-*- coding:utf-8 -*-
class TestClass(object):
	def __init__(self,name,age):
		self.name=name
		self.age=age
	def outname(self):
		print("age:%d"%self.age)


n=TestClass("wangxw",20)
if(hasattr(n,'name')):
	print("name:%s"%getattr(n,'name'))
if(hasattr(n,'score')):
	print("score:%d"%getattr(n,'score'))

if(hasattr(n,'outname')):
	fn=getattr(n,'outname')
	fn()