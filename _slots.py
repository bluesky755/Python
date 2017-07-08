#!/usr/bin/env python3
#--*-coding:utf-8 -*-
class Student(object):
	__slots__=('name','age')
	def __init__(self,name,age):
		self.name=name
		self.age=age
	def outputInfor(self):
		print("Name: %s Age:%d"%(name,age))

stu=Student('wangxw',40)
stu.score=20
stu.outputInfor()


