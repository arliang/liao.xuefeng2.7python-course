# -*- coding:utf-8 -*-
import itertools

#count
natuals = itertools.count(1)
#for n in natuals:
#	print n


#cycle()
cycle_1 = itertools.cycle('abc')
#for c in cycle_1:
#	print c

#repeat
repeat_1 = itertools.repeat('a',10)
for r in repeat_1:
	print r

#takewhile
count_1 = itertools.count(1)
count_1_limit = itertools.takewhile(lambda x:x <= 10,count_1)
for c in count_1_limit:
	print c

#chain()
for c in itertools.chain('abc','xyz'):
	print c

#groupby()  相邻的重复元素合并
for key,group in itertools.groupby('AAAABBBBCCCDDAA'):
	print key,list(group)

#imap

for x in itertools.imap(lambda x,y:x+y,[10,20,30],itertools.count(1)):
	print x

#ifilter
def odd_2(x):
	if x%2 == 0:
		return x
for x in itertools.ifilter(odd_2, [1,2,3,4,5,6]):
	print x

for x in itertools.ifilter(lambda x : x % 2 == 0,[1,2,3,4,5,6]):
	print x

