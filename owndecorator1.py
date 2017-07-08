#/usr/bin/env python
def log(func):
	def wrapper(*args,**dict1):
		print("start to execute %s" % func.__name__)
		func(*args,**dict1)
		print("end function %s" % func.__name__)
	return wrapper


@log
def test():
	print("this a programm used only for test")

test()