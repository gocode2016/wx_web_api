#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : classmate Lin.
# @Email   : 406728295@qq.com
# @File    : utils.py
# @Time    : 18-10-6 下午3:11


import hashlib
import time
import random


def md5_encrypt(raw_data):
    '''
    md5加密
    '''
    try:
        raw_data = raw_data.encode('utf-8')

        crypto_data = hashlib.md5(raw_data).hexdigest()

        return crypto_data

    except TypeError as e:
        print(e)
        raise


def time2timestamp(time_str):
    '''
    时间转时间戳
    '''
    timeArray = time.strptime(time_str, "%Y-%m-%d %H:%M:%S")
    timestamp = time.mktime(timeArray)

    return int(timestamp)

def timestamp2time(timestamp):

    timeArray = time.localtime(timestamp)
    otherStyleTime = time.strftime("%Y-%m-%d", timeArray)

    return otherStyleTime

def get_now_timestamp():
    '''
    获取当前时间戳
    '''
    return int(time.time())


def general_mch_order_id():
    char_list = [
        'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','y','x','w','z',
        '0','1','2','3','4','5','6','7','8','9'
    ]

    mch_order_id = ''.join(random.sample(char_list,20))

    return mch_order_id


def general_pay_body():
    body_list = ['c++','python','c','c#','php','perl','docker','mysql','mongdb','ruby','java']
    return f"网课胶囊:{random.choice(body_list)}入门到精通"


if __name__ == '__main__':
    print(general_pay_body())
    pass