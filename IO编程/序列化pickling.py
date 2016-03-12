# -*- coding:utf-8 -*-
#序列化 pickling 和 反序列化 unpickling
#两个模块  cPickle ：用c语言写 Pickle  ：纯python写
try:
	import cPickle as pickle
except ImportError:
	import pickle

import json




d = dict(name = 'klaus',age = 20,score = 88)
with open('./pickle.txt','wb') as open_file:
	pickle.dump(d,open_file)                        #把一个对象序列化并保存到一个文件里

read_d = open('./pickle.txt','rb')
load_d = pickle.load(read_d)
read_d.close()
print load_d                          #取出

#JSON
with open('./json.txt','wb') as json_d:
	json_d = json.dump(d,json_d)
print json_d




