def triangles(nline):
	line=nline
	pos=0
	while True:
		if pos>=line:
			break;
		else:
			yield getvalue(line,pos)
			pos+=1

def getvalue(line,pos):
	
	if pos<1 or pos>=line-1:
		return 1
	else:
		return getvalue(line-1,pos-1)+getvalue(line-1,pos)

print(list([x for x in triangles(6)]))


