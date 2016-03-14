#coding=utf-8
#multiprocessing:unix/linux 使用fork（）
#windows 使用multiprocessing 模块 提供process类来代表一个进程对象

from multiprocessing import Process,Queue,Pipe
from multiprocessing import Pool
import os,time,random

def run_proc(name):
	print 'Run child process %s (%s)..'%(name,os.getpid())

if __name__ == '__main__':
	print 'Parent process %s.'%os.getpid()
	p = Process(target = run_proc,args = ('test',))    #args  为一个tuple，故后面要加，号
	print  'Process will start'
	p.start()
	p.join()
	print 'Process end.'


# Pool
#用进城池的方式批量创建子进程
#pool.apply_async()用来向进程池提交目标请求

def long_time_task(name):
	print 'Run task %s (%s)...'%(name,os.getpid())
	start = time.time()
	time.sleep(random.random() * 3)    #random.random()用于生成一个0到1的随机符点数: 0 <= n < 1.0  推迟运行
	end =time.time()
	print 'Task %s runs %0.2f seconds.'% (name,(end - start))

if __name__ == '__main__':
	print 'Parent process %s.'% os.getpid()
	p = Pool()
	for i in range(5):
		p.apply_async(long_time_task,args = (i,))
	print 'waitting for all subprocesses done..'
	p.close()
	p.join()
	print 'All subprocesses done.'

#进程间的通信
#提供了Queue，Pipes

#写数据进程执行的代码
def write(q):
	for value in ['a','b','c']:
		print 'Put %s to queue ..'%value
		q.put(value)
		time.sleep(random.random())

#读数据进程执行的代码
def read(q):
	while True:
		value = q.get(True)
		print 'Get %s from queue '%value

if __name__ == '__main__':
	q = Queue()
	pw = Process(target=write,args=(q,))
	pr = Process(target=read,args=(q,))
	pw.start()
	pr.start()
	pw.join()
	pr.terminate()

