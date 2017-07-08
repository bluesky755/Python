#/usr/bin/env python
def move(n,a,b,c):
	if n==1:
		print ("Move 1 from %s==>%s" %(a,c))
	else:
		move(n-1,a,c,b)
		print("move single %d from %s==>%s" %(n,a,c))
		move(n-1,b,a,c);

num=input("Please input the qyt of disks to be moved:")
a="A"
b="B"
c="C"
move(num,a,b,c)


