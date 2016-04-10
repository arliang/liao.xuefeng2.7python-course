# -*- coding:utf-8 -*-
import struct
import re
print struct.pack('>I',10240099)
print struct.unpack('>IH','\xf0\xf0\xf0\xf0\x80\x80')
with open('./tree.bmp','rb') as tree:
	s = tree.read(30)

with open('./tree1.bmp','rb') as t1:
	b = t1.read(30)

print struct.unpack('<ccIIIIIIHH',b)
#('B', 'M', 47902, 0, 62, 40, 819, 460, 1, 1)
def bmpinfo(bmp):
	with open(bmp,'rb') as bmpimage:
		a = bmpimage.read(30)
	b = struct.unpack('<ccIIIIIIHH',a)
	if b[0] == 'B' and b[1] == 'M':
		return 'BMP size is %s * %s,BMP color is %s' %(b[6],b[7],b[-1])
	else:
		return 'that is no bmp file'



print bmpinfo('tree1.bmp')
print bmpinfo('tree.bmp')


