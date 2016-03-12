# -*- coding:utf-8 -*-
#try  ... except

try:
	print 'try...'
	r = 10 / 0
	print 'result:', r
except ZeroDivisionError, e:
	print 'except:' , e
finally:
	print 'finally...'

print 'end'

# a = 0 # a = 'a'    #不同赋值返回不同错误信息达到调试目的
a = 2
try:
	print 'try...'
	r = 10 / int(a)
	print  'result :', r
except ValueError, e:
	print 'ValueError:',e
except ZeroDivisionError,e:
	print 'ZeroDivisionError:',e
else:
	print 'No error'
finally:
	print 'finally...'
print 'END'

#调用堆栈
#err.py
def foo(s):
	return 10 / int(s)

def bar(s):
	return foo(s) * 2

def main():
	bar('0')
#main（）
#通过返回错误信息判断错误。
#记录错误  logging
import logging

def foo_2(s):
	return 10 / int(s)

def bar_2(s):
	return foo(s) * 2

def main_2():
	try:
		bar('0')
	except StandardError,e:
		logging.exception(e)

main_2()
print 'END'

#抛出错误

