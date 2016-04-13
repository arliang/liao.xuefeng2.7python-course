# -*- coding:utf-8 -*-
from gevent import monkey;monkey.patch_socket(),monkey;monkey.patch_all()
import gevent
import urllib2

#monkey patch的作用就是把urllib之类的io操作切换协程

def f(n):
	for i in range(n):
		print gevent.getcurrent(),i
		gevent.sleep(0)

g1 = gevent.spawn(f,5)
g2 = gevent.spawn(f,5)
g3 = gevent.spawn(f,5)
print g1
g1.join()
g2.join()
g3.join()

def g(url):
	print ('GET:%s'%url)
	resp = urllib2.urlopen(url)
	data = resp.read()
	print ('%d bytes received from %s.'%(len(data),url))

gevent.joinall([
	gevent.spawn(g,'https://www.python.org/'),
	gevent.spawn(g,'http://www.baidu.com/'),
	gevent.spawn(g,'http://www.sohu.com'),
])




