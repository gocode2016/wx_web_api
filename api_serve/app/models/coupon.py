#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : classmate Lin.
# @Email   : 406728295@qq.com
# @File    : coupon.py
# @Time    : 18-10-3 下午2:10

'''
优惠券
'''

from app.models.base import Base,db
from sqlalchemy import Column

class Coupon(Base):

    __tablename__ = 'coupon'

    id = Column(db.Integer,primary_key=True,autoincrement=True)

    #优惠金额
    coupon_money = Column(db.Integer)

    #用户编号
    user_id = Column(db.Integer,db.ForeignKey('users.user_id'))

    #优惠券
    coupon_code = Column(db.Integer)

    #优惠券状态,1待使用,0已使用
    coupon_status = Column(db.Integer)


    def __str__(self):
        return '优惠码:'+str(self.coupon_code)