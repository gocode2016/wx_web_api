#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : classmate Lin.
# @Email   : 406728295@qq.com
# @File    : __init__.py
# @Time    : 18-9-27 下午9:49


from flask import Blueprint

from app.api.v1.course import views as course_views
from app.api.v1.login import views as login_views
from app.api.v1.income import views as income_views
from app.api.v1.order import views as order_views
from app.api.v1.wxtoken import views as wxtoken_views

from app.api.v1.wxlogin import views as wxlogin_views
from app.api.v1.wallets import views as wallets_views
from app.api.v1.coupon import views as coupon_views

'''
蓝图定义
'''


def create_blueprint_v1():

    bp_v1 = Blueprint('v1',__name__)

    #使用优学院用户登录
    login_views.api.register(bp_v1)

    #获取课程详细信息
    course_views.api.register(bp_v1)
    #用户收入信息
    income_views.api.register(bp_v1)

    #订单查询，退款，微信支付回调接口等。
    order_views.api.register(bp_v1)

    #获取微信公众号基础服务accesstoken
    wxtoken_views.api.register(bp_v1)


    #微信用户登录
    wxlogin_views.api.register(bp_v1)

    #用户提现信息
    wallets_views.api.register(bp_v1)

    #用户优惠信息
    coupon_views.api.register(bp_v1)




    return bp_v1