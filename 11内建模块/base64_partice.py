# -*- coding:utf-8 -*-
import base64
B = base64.b64encode('binary\x00string')
print B
C = base64.b64decode('YmluYXJ5AHN0cmluZw==')
print C

print base64.b64encode('i\xb7\x1d\xfb\xef\xff')
#通过urlsafe然后编码后的字符可以作为参数在URL中被使用
print base64.urlsafe_b64encode('i\xb7\x1d\xfb\xef\xff')

#请写一个能处理去掉=的base64解码函数：
def safe_b64decode(args):
	if len(args) % 4 == 0:
		return base64.b64decode(args)
	elif len(args) % 4 == 1:
		return base64.b64decode(args+'===')
	elif len(args) % 4 == 2:
		return base64.b64decode(args+'==')
	else:
		print len(args)
		print '='.join(args)
		return base64.b64decode(args+'=')

'''
#同学的答案
def b6(str):
    return base64.b64decode(str+'='*(4-len(str)%4))
'''
print base64.b64encode('abcd')
print safe_b64decode('YWJjZA')
