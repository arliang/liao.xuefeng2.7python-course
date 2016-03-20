# -*- coding: utf-8 -*-
#定制类

# __str__    C.__str__(self)        可打印的字符串输出；内建 str() 及 print() 02函数

class student(object):
	def __init__(self,name):
		self.name = name

	def __str__(self):
		return 'Student object (name :%s)'% self.name
	__repr__ = __str__    #直接调用时也可以返回指定的类名，方法名

s = student('klaus')
print s

# __iter__  迭代    创建迭代类;内建 iter()
#斐波那契数列

class fib(object):
	def __init__(self):
		self.a,self.b = 0,1 #初始化

	def __iter__(self):
		return self   #实例本身是迭代对象

	def next(self):
		self.a,self.b =self.b ,self.a + self.b #下一个值
		if self.a > 20:#限制条件
			raise StopIteration()
		return self.a  #返回下一个值

f = fib()
for n in f:     #直接迭代出
	print n

# __getitem__
# #取某个值   得到单个序列元素

class Fib(object):
	def __init__(self):
		pass

	def __getitem__(self, item):
		a,b = 1,1
		for x in range(item):
			a,b = b,a + b
		return a


F = Fib()
print F[5]    #list切片

class fib_2(object):
	def __init__(self):
		pass
	def __getitem__(self, item):
		if isinstance(item,int):
			a,b = 1,1
			for x in range(item):
				a,b = b, a + b
			return a
		#slice 切片器
		if isinstance(item,slice):
			start = item.start
			stop = item.stop
			a,b = 1,1
			L = []
			for x in range(stop):
				if x >= start:
					L.append(a)
				a,b = b , a + b
			return L

b = fib_2()
print b[5]
print b[3:15]

#list 切片
print range(100)[10:20]

#__getattr__    C.__getattr__(self,attr)        获取属性；内建 getattr()；仅在属性没有找到时调用
class student_attr(object):

	def __init__(self):
		self.name = 'klaus'

	def __getattr__(self, attr):
		if attr ==  'score':
			return 99
		if attr == 'age':
			return lambda : 25
		#raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
a = student_attr()
print a.score
print a.age()
print a.abc

class chain(object):
	def __init__(self,path = ''):
		self._path = path

	def __getattr__(self, path):
		return chain('%s/%s'%(self._path,path))

	def __str__(self):
		return self._path

print chain().status.user.timeline.list

class chain_2(object):
	def __init__(self,path = ''):
		self._path = path


#__call__

class Chain_2(object):
	def __init__(self, path=''):
		self._path = path
	def __getattr__(self, path):
		return Chain_2('%s/%s' % (self._path, path))
	def __str__(self):        #返回路径
		return self._path
	def __call__(self,name):   #直接对实例调用
		return Chain_2('GET %s/%s'% (self._path,name))

print Chain_2().users('michael').repos







