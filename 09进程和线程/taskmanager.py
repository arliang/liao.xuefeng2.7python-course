#usr/bin/python
# -*- coding:utf-8 -*-
#filename: liaoxuefeng_fenbushijingcheng.py

import random,time,Queue
from multiprocessing.managers import BaseManager

task_queue=Queue.Queue()
result_queue = Queue.Queue()
class QueueManager(BaseManager):   #继承basemanager
    pass

#注册两个queue方法
QueueManager.register('get_task_queue',callable=lambda:task_queue)
QueueManager.register('get_result_queue',callable=lambda: result_queue)
print('........')
manager=QueueManager(address=('',5000),authkey=b'abc')
server=manager.get_server()
print('........')
server.serve_forever()

task=manager.get_task_queue()
result=manager.get_result_queue()