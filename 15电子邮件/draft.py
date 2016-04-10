# -*- coding:utf-8 -*-
import string
import re

to_addr_list = ['a@b.com','c@d.com']
to_addr_msg = ';'.join(to_addr_list)
print to_addr_msg

to_addr = ('moon.qiu@int-fly.com,moon.qiu198909@hotmail.com')
to_addr = string.splitfields(to_addr,",")
print to_addr


L = [x for x in range(512,560)]
str_L = [str(x) for x in L]
change_L = ['375235'+i+'@qq.com' for  i in str_L]
print change_L

'''
html_read = open('./python_org.html','rb')
print html_read.read()
'''

#第一种写法提取邮箱名
list1 = ('moon.qiu@int-fly.com,moon.qiu198909@hotmail.com')
cut_list = re.split(r'[\@\,]',list1)
finally_list = []
for x in range(0,len(cut_list)):
	if x % 2 == 0:
		finally_list.append(cut_list[x])
	else:
		continue
print finally_list
#第二种写法
cut_list_2 = [cut_list[x] for x in range(0,len(re.split(r'[\@\,]',list1))) if x % 2 == 0]
print cut_list_2

to_addr_1 = ('moon.qiu@int-fly.com,moon.qiu198909@hotmail.com')
to_addr_2 = string.splitfields(to_addr_1,",")
to_addr_3 = re.split(r'[\@\,]',to_addr_1)
'''
#两种方式，一种是将str的to_addr 转化为list类型以，号分割，另外一种是直接以list传入msg['TO']，起到发送多个邮箱的目的
to_addr = ['moon.qiu@int-fly.com', 'moon.qiu198909@hotmail.com']
'''
to_addr_list = [re.split(r'[\@\,]',to_addr_1)[x] for x in range(0,len(re.split(r'[\@\,]',to_addr_1))) if x % 2 == 0]

print to_addr_1
print to_addr_2
print to_addr_3
print to_addr_list

for index in range(1,5):
	print index