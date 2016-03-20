# -*- coding: utf-8 -*-

classmate = ['michael','bob','tracy']
print len(classmate)    #计算所含项数
print classmate[-1]     #最后一个
print classmate[::-1]   #逆序

classmate.append('moon')     #追加项
print classmate

classmate.insert(1,'jack')     #插入list指定位置
print classmate

print classmate.pop()      #删除指定项
print classmate

classmate[1] = 'zero'     #替换指定项的值
print classmate

#tuple：
classmates = ('301','302','303')
print classmates
try:
	classmates[1] = '305'
except:
	print 'error massege'     #检查代码是否异常，tuple无法修改删除，只能读取。较为安全

print len(classmates)

classmates_1 = ('304',)    #只有一个项的时候，需要在最后加一个逗号以示区分
