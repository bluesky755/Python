#/usr/bin/env python
# -*- coding:utf-8 -*-
'This is my first script written using python as a module'
__author__='Wang Xuewen'
import sys
def test():
	args=sys.argv
	if(len(args)==1):
		print('Hello,World!')
	elif(len(args)==2):
		print('Hello,%s'%args[1])
	else:
		print('Wrong args input!')

if __name__=='__main__':
	test()


