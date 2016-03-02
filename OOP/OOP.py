# !\usr\bin\env python
# -*- coding:utf-8 -*-
#OOP(面向对象语言)

class Student(object):
	def __init__ (self,name,score):
		self.name = name
		self.score = score

	def print_score(self):
		print '%s : %s'%(self.name,self.score)

#class 相当于一个模板
klaus = Student('Klaus Qiu','99')
lisa = Student('Lisa','88')
print klaus.score
print lisa.name




