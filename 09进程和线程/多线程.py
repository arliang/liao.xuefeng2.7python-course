# coding=utf-8
#多线程 一般使用threading
#Python的threading模块有个current_thread()02函数，它永远返回当前线程的实例。 current 现在的
import time,threading

#新线程执行的代码
def loop():
	print 'thread %s is running...'%threading.current_thread().name
	n = 0
	while n < 5:
		n = n + 1
		print 'thread %s >>> %s '% (threading.current_thread().name,n)
		time.sleep(1)
	print 'thread %s ended.' % threading.current_thread().name

print 'thread %s is running ...' % threading.current_thread().name
t = threading.Thread(target=loop,name = 'LoopThread')
t.start()
t.join()
print 'thread %s ended'% threading.current_thread().name

#Lock
balance = 0
lock = threading.Lock()

def change_it(n):
	global balance
	balance = balance + n
	balance = balance - n

def run_thread(n):
	for i in range(100000):
		lock.acquire()
		try:
			change_it(n)
		finally:
			lock.release()

t1 = threading.Thread(target=run_thread, args = (5,))
t2 = threading.Thread(target=run_thread, args = (8,))
t1.start()
t2.start()
t1.join()
t2.join()
print balance
print map(lambda x : x * x,[5])