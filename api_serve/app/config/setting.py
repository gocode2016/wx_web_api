#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : classmate Lin.
# @Email   : 406728295@qq.com
# @File    : setting.py
# @Time    : 18-9-27 下午9:46

'''
开发版本的设置
'''


import os

DEBUG = True

SECRET_KEY = os.urandom(24)

REDIS_CONFIG = {
  'CACHE_TYPE': 'redis',
  'CACHE_REDIS_HOST': '192.168.6.92',
  'CACHE_REDIS_PORT': 6379,
  'CACHE_REDIS_DB': '',
  'CACHE_REDIS_PASSWORD': '123456'
}


class MysqlConf:
    '''
    mysql 配置
    '''
    DB_USER = 'root'

    DB_PASS = '123456'

    DB_HOST = '192.168.6.92'

    DB_PORT = '3306'

    DB_NAME = 'test'

    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8".format(DB_USER, DB_PASS, DB_HOST, DB_PORT,
                                                                                   DB_NAME)

    SQLALCHEMY_TRACK_MODIFICATIONS = True

    SQLALCHEMY_COMMIT_TEARDOWN = True

WEIXIN_CONF = dict(
    WEIXIN_APP_ID = "",
    WEIXIN_APP_SECRET = "",
    MCH_ID = "1500104442",
    MCH_KEY = 'pass',
    WEIXIN_NOTIFY_URL="",
    WEIXIN_MCH_KEY_FILE="",
    WEIXIN_MCH_CERT_FILE=""
    )




class CsrfConf:
    '''csrf配置'''
    WTF_CSRF_ENABLED = False

#异步celery
#REDIS_URI = "redis://:123456@192.168.6.182:6379/0"
