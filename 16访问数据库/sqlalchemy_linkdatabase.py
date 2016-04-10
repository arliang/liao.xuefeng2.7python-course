# -*- coding:utf-8 -*-
from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.schema import ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from SQLAlchemy_practice import *

engine = create_engine('mysql+mysqlconnector://root:Password@localhost:3306/test')
DBSession = sessionmaker(bind=engine)

'''
#添加book数据
session = DBSession()
new_book = Book(id = '5',name = 'max limit4',user_id = '5')
session.add(new_book)
session.commit()
session.close()
'''
session = DBSession()
#one返回唯一行
book = session.query(Book).filter(Book.id == '1').one()
print 'type:',type(book)
print 'name:',book.name
print 'user_id:',book.user_id

user = session.query(User).filter(User.id == '6').one()
print 'type:',type(user)
print 'name:',user.name
book = session.query(Book).filter(Book.id == '1').one()
print 'type:',type(book)
print 'name:',book.name
print 'user_id:',book.user_id
#关闭连接
session.close()