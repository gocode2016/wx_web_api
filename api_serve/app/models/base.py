#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : classmate Lin.
# @Email   : 406728295@qq.com
# @File    : base.py
# @Time    : 18-9-28 上午11:02
'''
数据模型基类的定义
'''

from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy
from contextlib import contextmanager


class SQLAlchemy(_SQLAlchemy):

    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()

        except Exception as e:
            self.session.rollback()
            raise e



db = SQLAlchemy()


class Base(db.Model):

    __abstract__ = True


    '''
    do something
    '''


