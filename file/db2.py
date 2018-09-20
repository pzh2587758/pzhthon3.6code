# -*- coding: utf-8 -*-

"""
@version: ??
@author: djstava
@license: MIT Licence 
@contact: djstava@gmail.com
@site: http://www.xugaoxiang.com/blog
@software: PyCharm
@file: SQLAlchemy.py
@time: 2017/3/22 10:42
"""

from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

# 定义Channel对象:
class Channel(Base):

    # 表名
    __tablename__ = 'playback'

    # 表结构
    id = Column(String(20),primary_key=True)
    channel_name = Column(String(45))
    address = Column(String(80))
    service_name = Column(String(45))

    def __init__(self,id,channel_name,address,service_name):
        self.id = id
        self.channel_name = channel_name
        self.address = address
        self.service_name = service_name

# 初始化数据库连接,:
engine = create_engine('mysql+mysqlconnector://root:toor@localhost:3306/troutling')

print(engine)
