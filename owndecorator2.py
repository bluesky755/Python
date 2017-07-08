#/usr/bin/env python
def log(*alog):
	def decorator(func):
		def wrapper(*args,**dict1):
			print("start to execute %s" %(func.__name__))
			func(*args,**dict1)
			print("end function %s" % func.__name__)
		return wrapper
	return decorator


@log()
def test():
	print("this a programm used only for test")

test()