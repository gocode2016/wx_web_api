#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : classmate Lin.
# @Email   : 406728295@qq.com
# @File    : user.py
# @Time    : 18-9-28 下午12:18

'''
用户模型定义
'''

from app.models.base import Base,db
from sqlalchemy import Column,String,Integer
from sqlalchemy.exc import SQLAlchemyError

from app.models.lesson import Lessons
from app.models.order import Orders
from app.models.income import UserIncome,UserWallet
from app.models.spread import Spread
from app.models.coupon import Coupon

class Users(db.Model):

    __tablename__ = 'users'

    id = Column(db.Integer,primary_key=True,autoincrement=True)
    #优学院用户ID
    user_id = Column(db.Integer,unique=True)

    #优学院账号
    account = Column(db.String(100),unique=True,nullable=False)

    #优学院密码
    password = Column(db.String(100),nullable=False)

    #用户姓名
    realname = Column(db.String(20),nullable=True)

    #用户学校
    schoolname = Column(db.String(100),nullable=True)

    #
    mobile = Column(db.String(11),nullable=True)

    #登录时间
    login_time = db.Column(db.Integer)

    lesson = db.relationship('Lessons', backref='users',uselist=False)

    wxuser = db.relationship('WxUsers', backref='users',uselist=False)

    #orders = db.relationship('Orders',backref='users',uselist=False) #,lazy='dynamic'

    incomes = db.relationship('UserIncome',backref='users',uselist=False)

    wallets = db.relationship('UserWallet', backref='users', uselist=False)

    spread = db.relationship('Spread',backref='users',uselist=False)

    coupon = db.relationship('Coupon',backref='users',uselist=False)

    def __str__(self):
        return '用户编号: {}'.format(str(self.user_id))


    def __repr__(self):
        return '用户编号:{}'.format(str(self.user_id))
    # def __repr__(self):
    #     return str(self.user_id)

    def update(self):
        return session_commit()


    def add(self, user):
        db.session.add(user)
        return session_commit()




class WxUsers(Base):

    __tablename__ = 'wxusers'

    id = Column(db.Integer,primary_key=True,autoincrement=True)

    openid = Column(db.String(100))

    nickname = Column(db.String(100))

    user_id = Column(db.Integer,db.ForeignKey('users.user_id'))


    def __str__(self):
        return '微信编号'+str(self.user_id)

    def add(self, wxuser):
        db.session.add(wxuser)
        return session_commit()





def session_commit():
    try:
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
        reason = str(e)
        return reason