# -*- coding: utf-8 -*-
#map
def f(x):
	return x * x
print map(f,[1,2,3,4,5,6,7,8,9])
print map(float,[1,2,3,4,5,6,7,8,9])
print map(str,[1,2,3,4,5,6,7,8,9])

#reduce
def c(x,y):
	return x * y
print reduce(c,[1,2,3,4,5])

def fn(x,y):
	return x * 10 + y
print reduce(fn,[1,2,3,4,5])

def char2num(s):
	return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]  #dict
print reduce(fn,map(char2num,'13579'))

#整理一个str转化为int的函数
def str2int(s):
	def fn(x,y):
		return x * 10 + y
	def char2num1(s):
		return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
	return reduce(fn,map(char2num1,s))
print str2int('135')

#lambda 语句
def str2int1(s):
	return reduce(lambda x,y:x*10+y,map(char2num,s))

#利用map()函数，把用户输入的不规范的英文名字，
# 变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']。
def name(x):
	return x.title()
print map(name,['adam', 'LISA', 'barT'])

#Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积。

def prod(l):
	def product(x,y):
		return x * y
	if isinstance(l,list) == True:
		return reduce(product,l)
	else:
		pass

list1 = [1,2,3,4,5]
print prod(list1)
print isinstance(list1,list)

def other(b):
	if isinstance(b,list) == True:
		print "1"

b = ['1','2','3']
print other(b)


