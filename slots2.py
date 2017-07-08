#!/usr/bin/env python3
#-*-coding:utf-8 -*-
class parentc(object):
	@property
	def score(self):return self.__score
	@score.setter
	def score(self,value):
		self.__score=value
	#__slots__=('name','age')
class childc(parentc):
	__slots__=('name','age')

p=parentc()
c=childc()
p.score=80
c.score=88
print("c.score:%d"%c.score)