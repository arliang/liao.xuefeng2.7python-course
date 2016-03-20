# -*- coding:utf-8 -*-
import functools
print int ('12345',base=8)    #将str转化为INT
def int2(x,base=2):
	return int(x,base)

int2 = functools.partial(int,base = 2)   #函数需要固定参数时使用
print int2('100000')
print int2('15265',base = 10)   #也可以更改




