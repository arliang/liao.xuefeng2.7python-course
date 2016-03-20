# !/usr/bin/env python
# -*- coding:utf-8 -*-
#文件读写
import base64
desktop_path = 'C:/Users/moonq/Desktop'     #定义默认路径
f = open(desktop_path + '/bbbb.txt','w')      #创建新文本
f.write('hello')                          #写入str
f.close()            #保存关闭
with open(desktop_path + '/bbbb.txt','r') as r:     #注意r的时候为读取，w时候只能写入不能读
	print r.read()                                    #这样写不用加r.close去关闭文件

#二进制文件
#使用rb
with open(desktop_path + '/gbk.txt','w') as g:
	g.write('测试')
img = open(desktop_path + '/gbk.txt','rb')
change_img = img.read().decode('utf-8')
print change_img


#图片文字互转
#注意 import base64
with open(desktop_path + '/zhihu.jpg','rb') as image_flie:
	str = base64.b64encode(image_flie.read())               #将图片转化为文本
with open(desktop_path + '/zhihu_str.txt','w')  as image_str:
	image_str.write(str)                                                 #将文本写入文件

with open(desktop_path + '/str_image.png','wb') as str_file:
	str_file.write(str.decode('base64'))             #将文本转回图片







