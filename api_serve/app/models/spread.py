#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : classmate Lin.
# @Email   : 406728295@qq.com
# @File    : spread.py
# @Time    : 18-10-3 下午2:04

'''
用户推广
'''

from app.models.base import Base,db
from sqlalchemy import Column

class Spread(Base):

    __tablename__ = 'spread'

    id = Column(db.Integer,primary_key=True,autoincrement=True)

    user_id = Column(db.Integer,db.ForeignKey('users.user_id'))

    #分享码
    share_code = Column(db.Integer,nullable=False)

    #上级用户
    higher_upsn = Column(db.Integer,nullable=True)

    #报酬率,默认百分之5
    rate_of_pay = Column(db.Integer,nullable=False,default=5)


    def __str__(self):
        return "用户编号"+str(self.user_id)

