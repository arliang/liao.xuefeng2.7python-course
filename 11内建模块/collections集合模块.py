# -*- coding:utf-8 -*-
#namedtuple 一个函数，具有tuple的属性
from collections import namedtuple,defaultdict
from collections import deque,OrderedDict,Counter
Point = namedtuple('Point',['x','y'])
P = Point(1,2)
print P.x
print P.y
print isinstance(P,Point)
print isinstance(P,tuple)

#deque   方便添加删除元素  一个list
q = deque(['a','b','c'])
q.append('x')
q.appendleft('y')
q.popleft()
print q

#defaultdict
dict_d = defaultdict(lambda : 'N/A')
dict_d['key1']  = 'abc'
print dict_d['key1']
print dict_d['key2']

#OrderedDict  让dict的key排序
d = dict([('a',1),('b',2),('c',3)])
print d #无序排列
od_d = OrderedDict(d)
print od_d
od = OrderedDict([('a',1),('b',2),('c',3)])
print od

#利用OrderDict的特性做FIFO(先进先出)
class LastUpdateOrderedDict(OrderedDict):
	def __init__(self,capacity):
		super(LastUpdateOrderedDict,self).__init__()
		self._capacity = capacity

	def __setitem__(self, key, value):
		containsKey = 1 if key in self else 0
		if len(self) - containsKey >= self._capacity:
			last = self.popitem(last = False)
			print 'remove:',last
		if containsKey:
			del self[key]
			print 'set:',(key,value)
		else:
			print 'add:',(key,value)
		OrderedDict.__setattr__(self,key,value)

#counter  计数器，统计字符出现的个数

c = Counter()
for ch in 'programming':
	c[ch] =  c[ch] + 1

print c



