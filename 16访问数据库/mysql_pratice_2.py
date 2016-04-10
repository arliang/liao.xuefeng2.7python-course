import MySQLdb
conn= MySQLdb.connect(
        host='localhost',
        port = 3306,
        user='root',
        passwd='Password',
        )
cursor = conn.cursor()
cursor.execute('create database test')
