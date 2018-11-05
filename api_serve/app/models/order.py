#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : classmate Lin.
# @Email   : 406728295@qq.com
# @File    : order.py
# @Time    : 18-10-2 下午1:39

from app.models.base import Base,db
from sqlalchemy import Column
from datetime import datetime

from sqlalchemy.exc import SQLAlchemyError



class Orders(Base):

    __tablename__ = 'orders'

    id = Column(db.Integer,primary_key=True,autoincrement=True)

    #商户订单号
    mch_order_id = Column(db.String(100),unique=True,nullable=True)

    #用户编号
    user_id = Column(db.Integer)

    #微信订单号
    wx_order_id = Column(db.String(100),unique=True)

    # #用户编号
    # user_id = Column(db.Integer,db.ForeignKey('users.user_id'))

    #订单创建时间
    create_time = Column(db.DateTime,default=datetime.utcnow())

    #订单修改时间
    update_time = Column(db.DateTime,default=datetime.utcnow())

    #订单支付状态，未知-1，支付成功1，支付失败0
    pay_status = Column(db.Integer)

    #订单金额 单位分
    order_price = Column(db.Integer,default=15.0)


    #  #课程id
    # lesson_id = Column(db.Integer,db.ForeignKey('price.lesson_id'))

    #订单状态，是否完成
    order_status = Column(db.Integer)

    #
    lessons = db.relationship('Lessons', backref='orders', uselist=False)


    def __str__(self):
        return '商户单号：'+self.mch_order_id

    def add(self, order):
        db.session.add(order)
        return session_commit()

    def delete(self,order):
        db.session.delete(order)
        return session_commit()

    def update(self):
        return session_commit()

def session_commit():
    try:
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
        reason = str(e)
        return reason