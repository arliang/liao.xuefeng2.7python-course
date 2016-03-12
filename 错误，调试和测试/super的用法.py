# -*- coding: utf-8 -*-
#super 的用法
class A(object):
	def __init__(self):
		print 'enter A'
		print  'leave A'

class C(object):
	def __init__(self):
		print 'ENTER C'
		print 'LEAVE C'

class B(A):
	def __init__(self):
		print 'enter B'
		super(B, self).__init__()     #更改父类时，不用遍历更改
		print 'leave B'

b = B()