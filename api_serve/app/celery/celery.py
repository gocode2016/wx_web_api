#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : classmate Lin.
# @Email   : 406728295@qq.com
# @File    : celery.py
# @Time    : 18-10-8 下午2:42

'''
celery初始化
'''

from __future__ import absolute_import, unicode_literals

from celery import Celery
from app.config.secure import REDIS_URI


cel_app = Celery('app',
             broker=REDIS_URI,
             include=['app.celery.tasks'])

# # Optional configuration, see the application user guide.
# app.conf.update(
#     result_expires=3600,
# )

if __name__ == '__main__':
    cel_app.start()
