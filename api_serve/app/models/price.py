#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : classmate Lin.
# @Email   : 406728295@qq.com
# @File    : price.py
# @Time    : 18-10-3 上午10:28

from app.models.base import db,Base
from sqlalchemy import Column

class Price(Base):

    __tablename__ = 'price'

    id = Column(db.Integer,primary_key=True,autoincrement=True)

    #课程id
    lesson_id = Column(db.Integer,unique=True)

    # 课程名称
    lesson_name = Column(db.String(50), nullable=True)

    #每单元价格
    unit_price = Column(db.Integer,default=150)

    #全册价格
    all_price = Column(db.Integer,default=1500)


   # lesson = db.relationship('Lessons',backref='price',uselist=False)

    #order = db.relationship('Orders', backref='price', uselist=False)


    def __str__(self):
        return self.lesson_name + ':' + str(self.all_price)
