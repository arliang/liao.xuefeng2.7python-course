# -*- coding:utf-8 -*-
#序列化 pickling 和 反序列化 unpickling
#两个模块  cPickle ：用c语言写 Pickle  ：纯python写
try:
	import cPickle as pickle
except ImportError:
	import pickle

import json
import datetime




d = dict(name = 'klaus',age = 20,score = 88)
with open('./pickle.txt','wb') as open_file:
	pickle.dump(d,open_file)                        #把一个对象序列化并保存到一个文件里

read_d = open('./pickle.txt','rb')
load_d = pickle.load(read_d)
read_d.close()
print load_d                          #取出

#JSON
print json.dumps(d)    #dumps 和 dump的不同
# dumps()方法返回一个str，内容就是标准的JSON。类似的，dump()方法可以直接把JSON写入一个file-like Object。
json_str = json.dumps(d)
print json.loads(json_str)     #返回python的str

class Student(object):
	def __init__(self,name,age,score):
		self.name = name
		self.age = age
		self.score = score

	def student2dict(std):
		return {
			'name':std.name,
			'age':std.age,
			'score':std.score
		}

	def dict2student(d):
		return Student(d['name'], d['age'], d['score'])

b = Student('bob',20,88)
print json.dumps(b,default=Student.student2dict,sort_keys = True)
print json.dumps(b,default=lambda obj:obj.__dict__)    #用lambda方便

#object_hook 转回







