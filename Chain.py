#!/usr/bin/env python3
#-*- coding:utf-8-*-
class Chain(object):
	__path=''
	def __init__(self,path=''):
		self.__path=path
	def __getattr__(self,attr):
		if len(self.__path)==0:
			return Chain("%s"%(attr))
		else:
			return Chain("%s.%s"%(self.__path,attr))
	def __str__(self):
		return self.__path


print(Chain().my.folder.sublist.sublist1)
