# !/usr/bin/env python
# -*- coding:utf-8 -*-
import socket,time,threading

def tcplink(sock,addr):
	print 'accept new connection from %s:%s..'%addr
	sock.send('Welcome!')
	while True:
		data = sock.recv(1024)
		time.sleep(1)
		if data == 'exit' or not data:
			break
		sock.send('hello,%s!'%data)
	sock.close()
	print 'Connection from %s:%s closed.'%addr

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',9999))
s.listen(5)
print 'Waiting for connection...'

#永久循环
while True:
	sock,addr = s.accept()
	t = threading.Thread(target=tcplink,args=(sock,addr))
	t.start()
