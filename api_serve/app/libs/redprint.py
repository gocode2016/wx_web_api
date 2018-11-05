#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : classmate Lin.
# @Email   : 406728295@qq.com
# @File    : redprint.py
# @Time    : 18-9-27 下午9:48

'''
模仿蓝图实现的红图。
'''

class Redprint:
    '''
    红图
    '''
    def __init__(self, name):
        self.name = name
        self.mound = []

    def route(self, rule, **options):
        def decorator(f):
            self.mound.append((f, rule, options))
            return f

        return decorator

    def register(self, bp, url_prefix=None):

        if url_prefix is None:
            url_prefix = '/'+self.name

        for f, rule, options in self.mound:
            endpoint = self.name + '+' + options.pop("endpoint", f.__name__)

            bp.add_url_rule(url_prefix + rule, endpoint, f, **options)