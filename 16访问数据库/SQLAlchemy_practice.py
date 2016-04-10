# -*- coding:utf-8 -*-
from sqlalchemy import Column,String,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.schema import ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

#NOTICE!!!!!!:本节教程有误，已修改
#创建基类
Base = declarative_base()
#定义user对象
class User(Base):
    __tablename__ = 'user'
    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    # 一对多:
    books = relationship('Book')

class Book(Base):
    __tablename__ = 'book'
    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    # “多”的一方的book表是通过外键关联到user表的:
    user_id = Column(String(20), ForeignKey('user.id'))

#创建所有表
def createALL(engine):
    Base.metadata.create_all(engine)

def dropALL(engine):
    Base.metadata.drop_all(engine)

engine = create_engine('mysql+mysqlconnector://root:Password@localhost:3306/test')
DBSession = sessionmaker(bind=engine)

if __name__ == '__main__':
    createALL(engine)


