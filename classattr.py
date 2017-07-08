#!/usr/bin/env python
#-*- coding: utf-8 -*-
class fib(object):

	def __init__(self):
		self.a,self.b=0,1
		
	def __str__(self):
		return "Hello ,Current Class is fib"
	def __repr__(self):
		return "Hello,Current class is still fib"

	def __iter__(self):
		return self
	def next(self):
		self.a,self.b=self.b,self.a+self.b
		if self.a>1000:
			raise StopIteration()
		return self.a
	def __getitem__(self,n):
		a,b=1,1
		if isinstance(n,int):
			for x in range(n):
					a,b=b,a+b
			return a
		elif isinstance(n,slice):
			start=n.start
			end=n.stop
			if n.start==None:
				start=0
			L=[]
			for x in range(end):
				a,b=b,a+b
				if a>start:
					L.append(a)
			return L 



s=fib()
print(s[6])
print(s[2:5])
