#exercise of calculating BMI of Xiaoming
height=float(input("height:"))
weight=float(input("weight:"))

bmi=weight/height
BMI=bmi*bmi
print("BMI=%f" % bmi)
if BMI<18.5:
	print "too small"
elif BMI>=18.5 and BMI<25:
	print "normal"
elif BMI>=25 and BMI<28:
	print "Too heavy"
elif BMI>=28 and BMI<32:
	print "Fat"
else:
	print "serious fat"


