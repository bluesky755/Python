#!/usr/bin/env python3
#-*-coding:utf-8 -*-
class Chain(object):
	__path=''
	def __init__(self,path=''):
		self.__path=path
	def users(self,name):

		return Chain('/%s/:%s'%(name,name))
	def __getattr__(self,attr):
		return Chain('%s/%s'%(self.__path,attr))

	def __str__(self):
		return self.__path
	def __call__(self):
		print("I called my self!")



	__repr__=__str__

s=Chain()
Chain()