# -*- coding:utf-8 -*-
#class & instance


#数据封装
class Student(object):
	def __init__(self,name,score):
		self.name = name
		self.score = score

	def print_score(self):
		print '%s: %s' % (self.name, self.score)

	def print_name(self):
		print '%s'% self.name

	def get_grade(self):
		if self.score >= 90:
			return 'A'
		elif self.score <= 60:
			return 'C'
		else:
			return 'B'


lisa = Student('lisa',59)
bart = Student('bart emilison',60)

lisa.print_score()     #调用方式
bart.print_name()
print lisa.get_grade()

#访问限制
#def __private_name(self):   前面加单或双下划线
