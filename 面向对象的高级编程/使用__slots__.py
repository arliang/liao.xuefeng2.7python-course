# !/usr/bin/env python
# -*- coding: utf-8 -*-
from types import MethodType

class student(object):
	def __init__(self):
		pass



s = student()
s.name = 'klaus'  #为实例绑定一个属性
print s.name

def set_age(self,age):      #定义一个函数设置属性
		self.age = age

s.set_age = MethodType(set_age,s,student)     #给实例绑定一个方法
print s.set_age(25)
print s.age

def set_score(self,score):
	self.score = score

s2 = student()
s2.name = 'lisa'
student.set_score = MethodType(set_score,None,student)
print s.set_score(100)
print s.score
print s2.set_score(98)
print s2.score

#使用__slots__限制class属性
class student_2(object):
	__slots__ = ('name','age')
	def __init__(self):
		pass

s3 = student_2()
s3.name = 'jesu'
s3.age = '55'
# s3.score = 99    #AttributeError: 'student_2' object has no attribute 'score'受限无法放入

class grade_student(student_2):
	pass

s4 = grade_student()
s4.name = 'jay'
s4.score = 444

print s4.name
print s4.score    #无法继承


