#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : classmate Lin.
# @Email   : 406728295@qq.com
# @File    : cache.py
# @Time    : 18-10-7 下午7:14


from flask import request

from flask_cache import Cache


from app.config.secure import REDIS_CONFIG


cache = Cache(config=REDIS_CONFIG)


def make_cache_key(*args, **kwargs):

    path = request.path
    args = str(hash(frozenset(request.args.items())))
    return (path + args)


