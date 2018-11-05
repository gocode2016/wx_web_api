#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : classmate Lin.
# @Email   : 406728295@qq.com
# @File    : response.py
# @Time    : 18-10-6 下午12:40

'''
视图返回信息的封装
'''


def TrueReturn(data,msg):

    return {
        'status':True,
        'data':data,
        'msg':msg
    }



def FalseReturn(data,msg):

    return {
        'status':False,
        'data':data,
        'msg':msg
    }