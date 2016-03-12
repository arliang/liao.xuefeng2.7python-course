# -*- coding:utf-8 -*-
#操作文件和目录在python下
import os
import sys
#显示操作系统的名字：
os.name
#'posix' 未linux unix mac os x  如果是NT 则是windows系统

#环境变量
os.environ

#获得某个环境变量的值
os.getenv('PATH')

#查看当前目录的绝对路径
os.path.abspath('.')

#创建新目录
os.path.join('./','testdir')
os.mkdir('./testdir')
os.rmdir('./testdir')    #删除目录

#拆分路径

os.path.split('../OOP')
print os.path.splitext('../OOP/OOP.py')   #获取文件扩展名

#对文件重命名
with open('./bbbb.txt','w') as f:
	f.write('hello world.')
os.rename('bbbb.txt','test_1.py')
os.remove('test_1.py')

#列出当前目录下所有目录
C = [x for x in os.listdir('C:/') if os.path.isdir(x)]
print C

#列出所有py文件
D = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']
print D

#




