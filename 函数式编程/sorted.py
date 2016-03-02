# -*- coding: utf-8 -*-
#sorted
list = [1,3,4,8,9,5,9,6,2]
print sorted(list)   #从小到大排序
list.append('str')
print sorted(list)    #先数字后字符
list.append(None)
print sorted(list)    #先空集后数字
list.append('Str')
print sorted(list)   #先大写后小写

def reversed_cmp(x,y):
	if x > y:
		return -1
	elif x < y :
		return 1
	else:
		return 0     #sorted默认是用x>y 1 x<y-1. =0排序的,如果要相反，就让变量反向  查询cmp函数

print sorted(list,reversed_cmp)   #实现倒序排列
print sorted(list)[::-1]

def cmp_ignore(x,y):
	u1 = x.upper()
	u2 = y.upper()
	if u1 > u2:
		return 1
	elif u1 < u2:
		return -1
	else:
		return 0    #通过把字符upper然后再对比，出结果

list2 = ['apple','Banana','Cat','dog']


print sorted(list2)
print sorted(list2,cmp_ignore)

print cmp_ignore('ab','Ca')

l = ['bdwa','aawd','dyq','fkwr3']
print sorted(l,cmp_ignore)
