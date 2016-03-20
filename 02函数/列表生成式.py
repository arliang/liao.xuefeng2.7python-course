# -*- coding:utf-8 -*-
L = []
for n in range(1,11):
	L.append(n * n)
print L

#通过列表生成式
A = [x * x for x in range(1,12)]
print A

a = [x * x for x in range(1,12) if x % 2 == 0]   #加入判断语句筛选出偶数平方
print a

b = [m + n for m in 'xyz' for n in 'abc']     #双层循环输出所有组合
print b

import os
c = [d for d in os.listdir('..')]     #输出当前文件所在目录的所有文件   '.'为当前目录  '..'为上级目录
print c

#dict
d = {'x':'a','y':'b','z':'c'}
for k,v in d.iteritems():     #通过iteritems 迭代 dict
	print k ,'=', v

#通过列表生成式
e = [k+ '=' +v for k,v in d.iteritems()]    #+号起到连接符的作用。
print e

F = ['hello','WORLD','Apple',18,None]        #通过列表生成式生成所有可变字符串为小写
g = [s.lower() for s in F if isinstance(s,str) == True]
print g