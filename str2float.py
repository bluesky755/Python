#!/usr/bin/env python
from functools import reduce
def mapchars(s):
	def str2num(s):
		print [s]
		return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
	return map(str2num,s)

print(mapchars("234"))