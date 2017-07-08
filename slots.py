class student(object):

	def __init__(self,name,age):
		if not isinstance(name,str):
			
			raise ValueError("name is a string")
		if not isinstance(age,int):
			raise ValueError("age is a integer")
		self.__name=name
		self.__age=age

	def print_infor(self):
		print("Student:%s's score is:%d" %(self.__name,self.__age))


s=student('wangxw1',40)
s.print_infor()
