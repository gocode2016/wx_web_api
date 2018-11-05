#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : classmate Lin.
# @Email   : 406728295@qq.com
# @File    : admin.py
# @Time    : 18-10-5 下午7:49

from app.models.base import db,Base
from sqlalchemy import Column
from werkzeug.security import generate_password_hash,check_password_hash

class AdminUser(Base):
    '''
    管理员用户表
    '''

    __tablename__ = 'admin_user'

    id = Column(db.Integer,primary_key=True,autoincrement=True)

    #账号
    account = Column(db.String(30),unique=True)

    #密码
    password = Column(db.String(250))

    #邮箱
    email = Column(db.String(100))

    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    #返回密码哈希值
    def hash_password(self, password):
        return generate_password_hash(password)

    #验证密码哈希值是否正确
    def verify_password(self, password):
        return check_password_hash(self.password,password)


    def __str__(self):
        return '管理员: '+self.account