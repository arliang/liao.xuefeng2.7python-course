# -*- coding:utf-8 -*-
#关于多重继承

from SocketServer import TCPServer,ForkingMixIn,ThreadingMixIn


class animal(object):
	pass

class mammal(animal):
	pass

class bird(animal):
	pass

class runable(object):
	def run(self):
		print 'Running..'

class flyable(object):
	def fly(self):
		print 'Flying..'


class dog(mammal,runable):
	pass

class cat(mammal,runable):
	pass

class parrot(bird,flyable):
	pass

class ostrich(bird,flyable):
	pass


#mixin    通过定义类来添加其他额外的功能

class mytcpserver(TCPServer,ForkingMixIn):
	pass

