#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : classmate Lin.
# @Email   : 406728295@qq.com
# @File    : tasks.py
# @Time    : 18-10-8 下午2:42

'''
异步任务
'''
from __future__ import absolute_import, unicode_literals

from app.celery.celery import cel_app

@cel_app.task
def say_hi():
    print('hello world')

