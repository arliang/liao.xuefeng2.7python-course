# -*- coding: utf-8 -*-
#使用dict和set

#list:
names = ['michael','bob','tracy']
scores = [95,75,85]

#dict:
students = {'michael': 95,'bob' : 75,'tracy' : 85}    #注意使用大括号
print students
print students['michael']

students['jack'] = 88   #通过key直接添加
print students

print 'thomas' in students   #通过 in 判断 key是否在dict里
print students.get('ack')    #如果返回none 即没有该值
print students.get('jack')   #有该值的时候返回value
students.pop('jack')    #删除指定key
print students    #key必须为不可变对象

#set：
s =set([1,2,3,4])
print s
s1 = set([3,4,5,6])
print s & s1     #交集
print s | s1     #并集
s.add(7)
s.remove(1)
print s
