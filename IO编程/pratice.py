# -*- coding:utf-8 -*-
import sys
import os
#作业
#练习：编写一个search(s)的函数，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出完整路径：

def search(argv):
	__path = ['.']
	__file = []
	for i in __path:
		for x in os.listdir(i):
			if os.path.isdir(x):
				__path.append(x)
			if argv in x:
				__file.append(os.path.join(i,x))

	return __file

if __name__ == '__main__':
	for i in search(sys.argv[1]):
		print i

'''
def search(s):
    CurrentPath = os.path.abspath('.')
    L = [x for x in os.listdir('.') if os.path.isfile(x)]
    for fileName in L:
        if s in fileName:
            print os.path.join(CurrentPath, fileName)

search('m')


'''