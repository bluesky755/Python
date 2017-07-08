#/usr/bin/env python
def log(txt):
	def decorator(func):
		def wrapper(*args,**dict1):
			print('%s - %s' %(txt,func.__name__))
			return func(*args,**dict1)
		return wrapper
	return decorator


@log("Execute")
def test():
	print('this is a programme for test')

test()

