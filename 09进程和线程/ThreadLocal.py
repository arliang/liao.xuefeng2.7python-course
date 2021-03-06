# coding=utf-8
#ThreadLocal
#ThreadLocal最常用的地方就是为每个线程绑定一个数据库连接，HTTP请求，用户身份信息等，
# 这样一个线程的所有调用到的处理函数都可以非常方便地访问这些资源。

import threading
local_school = threading.local()

def process_student():
	print 'hello,%s (in %s)'%(local_school.student,threading.current_thread().name)
def process_thread(name):
	local_school.student = name
	process_student()

t1 = threading.Thread(target = process_thread,args = ('alice',),name = 'Thread-A')
t2 = threading.Thread(target= process_thread,args = ('bob',),name = 'Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
