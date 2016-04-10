# -*- coding:utf-8 -*-
import hashlib

md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?')
print md5.hexdigest()  #128bit


shal = hashlib.sha1()
#分次update也会胜场一样的结果
shal.update('how to use shal in')
shal.update('python hashlib?')
print shal.hexdigest() #160bit

#摘算算法应用
#作业一，计算出存储在数据库中的md5的口令：
def calc_md5(password):
	md5 = hashlib.md5()
	md5.update(password)
	return md5.hexdigest()

print calc_md5('123456')

#作业二：验证口令是否正确:
db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}
def login(user,password):
	if user in db.keys():
		md5 = hashlib.md5()
		md5.update(password)
		if md5.hexdigest() == db[user]:
			return 'login success!'
		else:
			print 'wrong password!'
	else:
		print 'user not exist!'

print login('michael','123456')
print login('bob','abc999')

#加盐
db = {}
def _get_md5(password):
	md5 = hashlib.md5()
	md5.update(password)
	return md5.hexdigest()

def register(username,password):
	if username in db.keys():
		return 'the username has exist.'
	else:
		db[username] = _get_md5(password + username + 'the-Salt')
		return 'register success.'

def loginWithSalt(username,password):
	if username in db.keys():
		if _get_md5(password + username + 'the-Salt') == db[username]:
			return 'login success'
		else:
			return 'fail to login'
	else:
		return 'username not exist!'

print register('klaus','123456')
print loginWithSalt('klaus','123456')
print loginWithSalt('klaus','654321')


