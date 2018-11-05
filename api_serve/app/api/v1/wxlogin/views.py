#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : classmate Lin.
# @Email   : 406728295@qq.com
# @File    : views.py
# @Time    : 18-10-6 下午10:25

'''
用户微信用户登录，
获取openid等信息.
'''
from app.libs.weixin import weixin
from weixin.login import WeixinLoginError

from app.config.secure import WEIXIN_CONF

from flask import request,redirect,url_for,jsonify

from app.libs.redprint import Redprint

from datetime import datetime,timedelta

from app.libs.response import TrueReturn,FalseReturn

from app.models.user import WxUsers

from app.forms.api.weixin import WxLoginForm

# weixin = WeixinLogin(WEIXIN_CONF['WEIXIN_APP_ID'],WEIXIN_CONF['WXIXIN_APP_SECRET'])



api = Redprint('wxlogin')


class WxUserView:

    @staticmethod
    @api.route("",methods=['POST'])
    def wx_login():

        form = WxLoginForm.create_api_form()
        form.validate()

        code = form.code.data
        user_id = form.user_id.data
        try:
            data = weixin.access_token(form.code.data)
            openid = data.openid
            '''
            获取用户信息
            '''
            wxuser = WxUsers(openid=openid,user_id=user_id,nickname='')
            WxUsers.add(WxUsers,wxuser)


        except WeixinLoginError:
            return jsonify(FalseReturn('','invalid code.'))


        return jsonify(TrueReturn('','登录成功.'))