# -*- coding: utf-8 -*-
#type()


class hello(object):
	def __init__(self):
		pass
	def hello(self,name = 'world'):
		return ('hello,%s.') % name

h = hello()
print h.hello()
print h.hello('klaus')
print type(hello)
print type(h)

def  fn(self,name = 'world'):    #先创建一个函数
	print 'hello,%s'% name

hello_1 = type('hello',(object,),dict(hello = fn))     #创建class，名称，父类，方法

h = hello_1()
print h.hello
print type(hello)
print type(h)