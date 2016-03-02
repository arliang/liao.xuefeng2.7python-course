# -*- coding:utf-8 -*-
#__future__ module
#2.x里的字符串用'xxx'表示str，Unicode字符串用u'xxx'表示unicode，而在3.x中，所有字符串都被视为unicode,b'xxx'才表示str
from __future__ import unicode_literals
from  __future__ import division

print '\'xxx\' is unicode?',isinstance('xxx',unicode)   #判断在version 2.7下 xxx是否为unicode
print 'u\'xxx\'is unicode?',isinstance(u'xxx',unicode)
print '\'xxx\'is str?',isinstance('xxx',str)
print 'b\'xxx\'is str?',isinstance(b'xxx',str)

#python2.7下
print 10/3     #地板除
print 10.0/3    #精确除法

#python3.x下
print '10 / 3 =',10/3    #精确除
print '10 // 3 =',10//3   #地板除