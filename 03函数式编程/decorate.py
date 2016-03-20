# -*- coding: utf-8 -*-
import time

def now():
	return time.localtime()

f = now
print f
print f()

print now.__name__
print f.__name__

#decorator 是一个返回函数的高阶函数

def log(func):
	def wrapper(*args,**kw):
		print 'call %s():'% func.__name__
		return func(*args,**kw)
	return wrapper

@log
def now():
	return 'now:%s'%time.localtime()    #会先调用log

print now()

def log(text):
	def d(func):
		def wrapper(*args,**kw):
			print  '%s:%s()'%(text,func.__name__)
			return func(*args,**kw)
		return wrapper
	return d                            #三层嵌套


@log('test')
def now():
	return time.localtime()

print now()
print now.__name__     #最终返回的是wrapper函数

import functools


def log1(func):
	@functools.wraps(func)     #将function属性重定回now
	def wrapper(*args,**kw):
		print 'call %s():'% func.__name__
		return func(*args,**kw)
	return wrapper

@log1
def now1():
	return time.localtime()

print now1()
print now1.__name__       #将function属性重定回now

#作业
import functools

def log2(text):
	if callable(text):
		@functools.wraps(text)
		def wrapper(*args,**kw):
			print 'begin call:%s'%text.__name__
			print  'function:%s'% text(*args,**kw)
			return 'end call:%s'%text.__name__
		return wrapper
	else:
		def d(func):
			@functools.wraps(func)
			def wrapper(*args,**kw):
				print 'begin call:%s'%func.__name__
				print 'function:%s,%s'% (func(*args,**kw),text)
				return 'end call:%s'%func.__name__
			return wrapper
		return d


@log2
def f1():
	return 1

@log2('execute')
def f2():
	return 1



print f1()
print f2()



def log3(text):
    if callable(text):     #使用callable判断args是否为函数 如果为True 执行
        @functools.wraps(text)
        def wrapper(*args, **kw):
            print 'begin call: ' + text.__name__
            text(*args, **kw)
            print 'end call: ' + text.__name__
        return wrapper
    else:
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print 'begin call: ' + text
                func(*args, **kw)
                print 'end call: ' + text
            return wrapper
        return decorator

@log3
def  f3():
    print 'doing1...'

@log3('text')
def f4():
    print 'doing2...'


print f3()
print f4()
