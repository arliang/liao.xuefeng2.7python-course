# !/usr/bin/env  python
# -*- coding: utf-8 -*-
'a test module'

__author__ = 'Klaus Qiu'
import sys

def test():
	args = sys.argv
	if len(args) == 1:
		return 'hello world'
	elif len(args) == 2:
		return 'hello,%s' %args[1]
	else:
		return 'too many argvment input'

if __name__=='__main__':
    test()

try:
	import cStringIO as StringIO      #设置别名
except ImportError:
	import StringIO     #如果失败导入StringIO

try:
	import json    # python version >= 2.6
except ImportError:
	import simplejson as json    #python version <= 2.5

#private 私有
def _private1(x):       #定义私有函数
	return 'hello,%s'%x

def _private2(x):
	return '%s'%x

def pulic(name):     #使用公有函数调用私有函数
	if len(name) >= 3:
		return _private1(name)
	else:
		return _private2(name)


from PIL import Image
dj = Image.open('dj.jpg')
print dj.format,dj.size,dj.mode
dj.thumbnail((200,100))
dj.save('dj_2.jpg','jpeg')



