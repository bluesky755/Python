#!/usr/bin/dev python3
#-*- coding:utf-8 -*-
import sys
class Fib(object):
	a,b=0,1
	def __init__(self,m):
		self.m=m
	def __iter__(self):
		return self
	def __next__(self):
		self.a,self.b=self.b,self.a+self.b
		if self.a>self.m:
			raise StopIteration();
		return self.a

s=Fib(int(sys.argv[1]))
for i in s:
	print(i)
