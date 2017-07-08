#!/usr/bin/env python
def NameConvert(s):	
	return s.capitalize()

names=["jack","mary","Mike"]
L=list(map(NameConvert,names))
print(L)