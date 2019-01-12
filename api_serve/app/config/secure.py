#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : classmate Lin.
# @Email   : 406728295@qq.com
# @File    : secure.py
# @Time    : 18-9-27 下午9:46

'''
生产版本的配置
'''

import os

SECRET_KEY = os.urandom(24)

REDIS_CONFIG = {
  'CACHE_TYPE': 'redis',
  'CACHE_REDIS_HOST': '',
  'CACHE_REDIS_PORT': 6379,
  'CACHE_REDIS_DB': '',
  'CACHE_REDIS_PASSWORD': ''
}


class MysqlConf:
    '''
    mysql 配置
    '''
    DB_USER = ''

    DB_PASS = ''

    DB_HOST = ''

    DB_PORT = ''

    DB_NAME = ''

    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8".format(DB_USER, DB_PASS, DB_HOST, DB_PORT,
                                                                                   DB_NAME)

    SQLALCHEMY_TRACK_MODIFICATIONS = True

    SQLALCHEMY_COMMIT_TEARDOWN = True

WEIXIN_CONF = dict(
    WEIXIN_APP_ID = "",
    WEIXIN_APP_SECRET = "",
    MCH_ID = "",
    MCH_KEY = '',
    WEIXIN_NOTIFY_URL="",
    WEIXIN_MCH_KEY_FILE="",
    WEIXIN_MCH_CERT_FILE=""
    )




class CsrfConf:
    '''csrf配置'''
    WTF_CSRF_ENABLED = True

#异步celery
#REDIS_URI = "redis://:123456@192.168.6.182:6379/0"
