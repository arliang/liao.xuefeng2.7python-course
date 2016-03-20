# -*- coding: utf-8 -*-
import math
print math.cos(5)
print abs(-1100)   #内置函数直接调用
print cmp(3,4)     #当x < y 时输出-1
print cmp(4,1)     #当x > y 时输出1
print cmp(3,3)     #当 x = y 时输出0

def my_abs(x):
	if not isinstance(x,(int,float)):
		raise TypeError('bad operand type')    #添加类型判断
	if x < 0:
		return -x
	else:
		return x

print my_abs(5)
print my_abs(-5)

def move(x,y,step,angle=0):
	nx = x + step * math.cos(angle)
	ny = y + step * math.sin(angle)
	return nx,ny

print move(2,3,4,30)

#可变参数
def calc(numbers):
	sum = 0
	for n in numbers:
		sum =  sum + n * n
	return sum

print calc([1,2,3])     #必须是list或者tuple的形式

def calc_1(*numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n
	return sum

print calc_1(1,2,3)    #可变函数可以随意

def person(name,age,**kw):
	print "name:",name,"age:" ,age,"other:",kw
	return kw
print person("klaus",18)
print person("moon",27,city ="guangzhou")     #关键字参数


#参数组合
def func(a,b,c = 0, *args,**kw):
	print 'a=',a,'b=',b,'c=',c,'args=',args,'kw=',
	return kw
print func(1,2)
print func(1,2,c=3)
print func(1,2,3,'a','b',x=99)