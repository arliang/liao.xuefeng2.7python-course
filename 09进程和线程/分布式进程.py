# coding=utf-8
#taskmanager.py
'''
import random,time,Queue
from multiprocessing.managers import BaseManager

#发送任务的队列
task_queue = Queue.Queue()

#接受结果的队列
result_queue = Queue.Queue()

#从basemanager 继承的QueueManager
class QueueManager(BaseManager):
	pass

#把两个queue都注册到网络上，callable参数关联了queue对象
QueueManager.register('get_task_queue',callable=lambda :task_queue)
QueueManager.register('get_result_queue',callable=lambda :result_queue)

#绑定端口5000，设置验证码为‘abc'
manager = QueueManager(address=('',5000),authkey='abc')

#启动Queue：
manager.start()

#获得通过网络访问的queue对象：

task  = manager.get_task_queue()
result = manager.get_result_queue()

#放任务：
for i in range(10):
	n = random.randint(0,10000)
	print ('put task %d...'%n)
	task.put(n)
#从result队列读取结果：
print ('Try get results..')
for i in range(10):
	r = result.get(timeout = 10)
	print('Result:%s'%r)

#shutdown
manager.shutdown()
'''

#有bug