# -*- coding: utf-8 -*-

import mysql.connector
#创建数据库test
'''
conn = mysql.connector.connect(user = 'root',password = 'Password',use_unicode = True)
cursor = conn.cursor()
cursor.execute('create database test')
'''
#创建后连接
conn = mysql.connector.connect(user = 'root',password = 'Password',database = 'test',use_unicode = True)
cursor = conn.cursor()

cursor.execute('create table user (id VARCHAR (20) PRIMARY KEY ,name VARCHAR (20))')
cursor.execute('insert into user (id,name )values (%s,%s)',['1','klaus'])
cursor.rowcount
conn.commit()
cursor.close()
cursor = conn.cursor()
cursor.execute('select * from user where id = %s',('1',))
values = cursor.fetchall()
print values
cursor.close()
conn.close