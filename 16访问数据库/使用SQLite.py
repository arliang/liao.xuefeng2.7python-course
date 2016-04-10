# !/usr/env/bin python
# -*- coding:utf-8 -*-
import sqlite3
conn = sqlite3.connect('test.db')
#通过游标操作插入数据库并插入数据
'''
cursor = conn.cursor()
cursor.execute('create table user (id varchar(20) PRIMARY key ,name VARCHAR (20))')
cursor.execute('insert into user (id,name) values (\'1\',\"klaus\")')
cursor.rowcount
cursor.close()
conn.commit()
conn.close()
'''
cursor = conn.cursor()
cursor.execute('SELECT * from user where id = ?',('1',))
values = cursor.fetchall()
print values
cursor.close()
conn.close()
