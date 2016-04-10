# -*- coding:utf-8 -*-
import __future__
import re

#\d 匹配数字
#\w 匹配数字和字母
# *表示任意个字符，+表示至少一个字符，？表示0个或1个
#\s 匹配一个空格
value = 'bill.gates@microsoft.com,moon.qiu@int-fly.com,moon.qiu198909@hotmail.com'
#if re.match(r'^(\w+?\S+?)\@(\w+?).(\w+?)$',value):
if re.match(r'(\w+?\S+?)\@(\w+?)\.(\w+?)', value):
	print value
else:
	print 'not a mailbox address'

value_2 = '<Tom Paris> tom.dd@voyager.org'
#if re.match(r'^<(.+?)> (\w+?\S+?)@(\w+?.\w+?)$',value_2):
if re.match(r'<.+?>\s(\w+?\S+?)@(\w+?\.\w+?)', value_2):
	print value_2
else:
	print 'not a mailbox address'


#切分字符串
L = ('a d ::  ,, d')
print re.split(r'[\,\s\;\:]+', L)
print re.split(r'[\s\,\;]+', 'a,b;; c  d')

a='Beautiful, is; better*than\nugly'
print re.split(r'[\s\,\:\*]+', a)   #空格，逗号，分号，星号为标准匹配到即分离

#贪婪匹配
#加？可以让表达式变为非贪婪匹配
print re.match(r'(\d+?)(0*)$', '10230000').groups()

#预编译
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
#使用
print re_telephone.match('010-22323').groups()

