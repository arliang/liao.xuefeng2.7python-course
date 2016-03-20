# -*- coding: utf-8 -*-
#create list:
L = [x for x in range(0,11)]
print L

#create generator
g = (x for x in range(0,11))
print g.next()

#斐波拉契数列
def fib(max):
	n,a,b = 0,0,1
	while n < max:
		yield b           #通过yield把结果生成为generator
		a,b = b, a+b
		n = n + 1

print [s for s in fib(6)]    #通过循环迭代生成器