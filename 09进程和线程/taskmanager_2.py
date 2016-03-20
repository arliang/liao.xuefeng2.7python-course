#usr/bin/python
#filename: laioxuefeng_fenbuhi-two.py
#coding=utf-8
import taskmanager as fbs
import time,random
from multiprocessing.managers import BaseManager

class QueueManager(BaseManager):
    pass

QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

server_addr='127.0.0.1'
print('connet to server %s' %server_addr)

m=QueueManager(address=(server_addr,5000),authkey=b'abc')

m.connect()
task=m.get_task_queue()
result=m.get_result_queue()

for i in range(10):
    n=random.randint(0,10000)
    print('Put task %s' %n)
    task.put(n)