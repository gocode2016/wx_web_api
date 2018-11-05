#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : classmate Lin.
# @Email   : 406728295@qq.com
# @File    : views.py
# @Time    : 18-10-6 下午10:30

'''
获取用户优惠信息
'''

from app.libs.redprint import Redprint
from flask import request,jsonify

from app.libs.auth import Auth
from app.forms.api.coupon import CouponForm

from app.libs.response import TrueReturn,FalseReturn

from app.models.coupon import Coupon

from app.libs.cache import cache,make_cache_key

api = Redprint('coupon')


class CouponView():

    @staticmethod
    @api.route('',methods=['GET','POST'])
    @cache.cached(timeout=60*10,key_prefix=make_cache_key)
    def coupon_view():

        result = Auth.identify(Auth,request)

        #未通过token认证返回错误信息
        if result['status'] == False:
            return jsonify(result)

        form = CouponForm().create_api_form()
        form.validate()

        coupons = Coupon.query.filter_by(user_id=form.user_id.data).all()

        if len(coupons) == 0:
            return jsonify(FalseReturn('','暂无优惠码.'))

        res = []

        for cou in coupons:
            temp = {"coupon_code":cou.coupon_code,
                    "coupon_money":cou.coupon_money,
                    "coupon_status":cou.coupon_status}
            res.append(temp)

            del temp

        data = {
            "coupon":res
        }
        return jsonify(TrueReturn(data,msg='请求成功',))
