#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : classmate Lin.
# @Email   : 406728295@qq.com
# @File    : lesson.py
# @Time    : 18-10-2 下午1:24

from app.models.base import Base,db
#from app.models.user import Users
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import Column
from datetime import datetime

class Lessons(Base):

    __tablename__ = 'lessons'

    # 自增长id
    id = Column(db.Integer, primary_key=True, autoincrement=True)

    #商户订单编号
    mch_order_id = Column(db.String(100),db.ForeignKey('orders.mch_order_id'))

    #微信订单号
   # wx_order_id = Column(db.String(100),db.ForeignKey('orders.wx_order_id'))

    # 外键,对应users表的userid
    user_id = Column(db.Integer, db.ForeignKey('users.user_id'))

    # 课程id
    lesson_id = Column(db.Integer)

    # 课程名称
    #lesson_name = Column(db.String(50), nullable=True)

    # 最近代做时间
    update_time = Column(db.DateTime, default=datetime.utcnow())

    # 需要代做的次数,定时任务可能会用上。
    do_count = Column(db.Integer, default=0)

    is_all = Column(db.Boolean,default=0)

    start_unit = Column(db.Integer,default=0)

    end_unit = Column(db.Integer,default=0)

    # 代做周期类型,
    do_time_type = Column(db.Integer, default=0)

    #是否完成
    is_ok = Column(db.Boolean)

    def add(self, lesson):
        db.session.add(lesson)
        return session_commit()

    def delete(self,lesson):
        db.session.delete(lesson)
        return session_commit()


def session_commit():
    try:
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
        reason = str(e)
        return reason