#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : classmate Lin.
# @Email   : 406728295@qq.com
# @File    : income.py
# @Time    : 18-10-3 上午10:08


from app.models.base import db,Base
from sqlalchemy import Column
from datetime import datetime


class UserWallet(Base):

    '''
    用户钱包
    '''
    __tablename__ = 'wallet'

    id = Column(db.Integer,primary_key=True,autoincrement=True)

    user_id = Column(db.Integer,db.ForeignKey('users.user_id'))

    #未提现
    not_put_forward = Column(db.Integer,default=0)

    #已提现
    already_preseted = Column(db.Integer,default=0)

    #提现中
    withdraw_cashint = Column(db.Integer,default=0)


class UserIncome(Base):
    '''
    收入明细
    '''
    __tablename__ = 'income'

    id = Column(db.Integer,primary_key=True,autoincrement=True)

    user_id = Column(db.Integer,db.ForeignKey('users.user_id'))

    #收入金额
    income_price = Column(db.Integer)

    #收入来源
    from_user = Column(db.Integer)

    #日期
    income_time = Column(db.DateTime,default=datetime.utcnow())