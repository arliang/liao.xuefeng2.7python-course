# -*- coding: utf-8 -*-
#lambda
print map(lambda x:x * x,[1,2,3,4,5,6])

def build(x,y):
	return lambda :x * x + y * y

print build(1,2)
f = build(1,2)
print f()      #先定义，后调用