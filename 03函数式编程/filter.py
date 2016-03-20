# -*- coding: utf-8 -*-
# filter

L = []
for s in range(0,101):
	L.append(s)
print L                  #先创建一个list

def is_odd(x):
	if  x % 2 == 0:
		return x
print filter(is_odd,L)     #将一个函数的作用于每一个value，然后根据函数的条件输出

odd = []
for x in range(2,101):
	for y in range(2,x):
		if x % y == 0:
			break
	else:
		odd.append(x)
print odd                    #输出所有素数

def no_odd(x):
	if x < 2:
		return x
	elif x in odd:      #判断是否在素数表里
		pass
	else:
		return x
print filter(no_odd,L)      #自己写的关于filter的作业，输出所有非素数 range（0-100）

def isPrime(s):
	if s < 2:
		return s
	else:
		for x in range(2,s):
			if s % x == 0:
				return s    #判断是否为素数，不是便输出

print filter(isPrime,range(1,101))

def prime(s):
	if 1 < s < 3:
		return s
	elif s == 1:
		pass
	else:
		for x in range(3,s):
			if s % x == 0:
				break
		else:
			return s    #判断是否为素数，是就输出
print filter(prime,range(1,20))

