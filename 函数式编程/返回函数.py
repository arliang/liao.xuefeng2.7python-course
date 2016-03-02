# -*- coding: utf-8 -*-
#返回函数

#求和函数的基本定义
def calc_sum(*args):
	ax = 0
	for n in args:
		ax = n + ax
	return ax

#返回求和的函数
def lazy_sum(*args):
	def sum():
		ax = 0
		for n in args:
			ax = ax + n
		return ax
	return sum
print lazy_sum(1,3,4,5,6)     #返回一个<function sum at 0x02CF9830>求和函数
f = lazy_sum(1,3,4,5,6)
print f()       #调用函数f时，才返回求和结果

#闭包
def count():
	fs = []
	for n in range(1,4):
		def f():
			return n * n
		fs.append(f)
	return fs
f1,f2,f3 = count()
print f1(),f2(),f3()   #f1,f2,f3为函数  f1(),f2(),f3()才为值

def count_1():
	fs_1 = []
	for n in range(1,4):
		def f(n):
			def g():
				return n * n
			return g
		fs_1.append(f(n))
	return  fs_1
f4,f5,f6 = count_1()
print f4(),f5(),f6()
