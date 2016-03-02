# !\usr\bin\env python
# -*- coding:utf-8 -*-
#使用 @property

class student(object):
	def __init__(self):
		pass

	def get_score(self):
		return self._score

	def set_score_value(self,value):
		if isinstance(int(value),int) == False:
			raise ValueError('It must be an integer!')
		elif isinstance(int(value),int) == True:
			if int(value) < 0 or int(value) > 100:
				raise ValueError('score must between 0~100!')
			else:
				self._score = value
		else:
			raise ValueError('It must be an integer!')

'''
	def set_score_value(self,value):
		if not isinstance(value,int):
			raise ValueError('it must be an integer!')
		elif value < 0 or value > 100:
			raise ValueError('score must between 0~100!')
		else:
			self._score = value           #原教程没有判断当str可以转化为INT的情况，上面已补充
'''





s = student()
s.set_score_value('88')    #通过函数赋值
print s.get_score()

# s.set_score_value(3333)  #报错

# @property
class Student(object):
	def __init__(self):
		pass

	@property
	def score(self):
		return self._score

	@score.setter
	def score(self, value):      #变成属性赋值
		if not isinstance(value, int):
			raise ValueError('score must be an integer!')
		if value < 0 or value > 100:
			raise ValueError('score must between 0 ~ 100!')
		self._score = value

b = Student()
b.score = 61    #通过属性直接复制
print b.score



