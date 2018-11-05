#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : classmate Lin.
# @Email   : 406728295@qq.com
# @File    : views.py
# @Time    : 18-10-5 下午10:27


'''
用户获取基础服务支持的access_token,跟获取openid的同时得到的access_token不同.
'''

from flask import request,jsonify

from app.libs.redprint import Redprint
from app.libs.response import TrueReturn,FalseReturn

from app.config.secure import WEIXIN_CONF

from app.libs.cache import cache,make_cache_key

import requests

api = Redprint('wxtoken')

def get_wx_access_token(APPID,APPSECRET):

    url = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid="+ APPID + "&secret=" + APPSECRET
    try:
        res = requests.get(url).json()
        return res
    except:
        return None


class AccessTokenView:
    '''
    获取access_token,token维护暂未完成
    '''
    @staticmethod
    @api.route('',methods=['GET'])
    @cache.cached(timeout=7000,key_prefix=make_cache_key)
    def access_token():
        APPID = WEIXIN_CONF['WEIXIN_APP_ID']
        APPSECRET = WEIXIN_CONF['WXIXIN_APP_SECRET']

        res = get_wx_access_token(APPID,APPSECRET)

        if res is None:
            return jsonify(FalseReturn('','未知错误.'))

        if "access_token" in res:
            res_data = {
                "access_token":res["access_token"]
            }

            return jsonify(TrueReturn(res_data,'请求成功.'))


        return jsonify(FalseReturn(res,'请求失败'))