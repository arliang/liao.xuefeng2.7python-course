# !\usr\bin\env python
# -*- coding:utf-8 -*-
class animal(object):
	def __init__(self):
		pass

	def run(self):
		print 'Animal is running..'

	def run_twice(animal):
		animal.run()
		animal.run()
		

class dog(animal):
	def run(self):
		print 'Dog is running'

	def eat(self):
		print 'Dog eating meat'


class cat(animal):
	def run(self):
		print 'Cat is running'
		
		
class tortoise(animal):
	def run(self):
		print 'tortoise is running slowly.'

animal = animal()
animal.run()

dog = dog()
dog.run()        #先执行子类同名函数
dog.run_twice()    #多态。继承
tortoise.run_twice()  




