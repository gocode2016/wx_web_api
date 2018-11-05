#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : classmate Lin.
# @Email   : 406728295@qq.com
# @File    : views.py
# @Time    : 18-10-5 下午10:30

'''
用户收入信息,
'''

from app.libs.redprint import Redprint
from app.forms.api.income import IncomeForm

from app.models.income import UserIncome
from app.models.user import Users
from app.libs.response import TrueReturn,FalseReturn
from flask import jsonify,request
from app.libs.utils import time2timestamp
from app.libs.auth import Auth
from app.libs.cache import cache,make_cache_key
api = Redprint('income')


class IncomeView:

    @staticmethod
    @api.route('',methods=['POST','GET'])
    @cache.cached(timeout=60*10,key_prefix=make_cache_key)
    def get_income():

        result = Auth.identify(Auth,request)

        #未通过token认证返回错误信息
        if result['status'] == False:
            return jsonify(result)


        form = IncomeForm.create_api_form()
        form.validate()

        try:
            user_id = form.user_id.data

            #coupons = Coupon.query.filter_by(user_id=form.user_id.data).all()
            incomes = UserIncome.query.filter_by(user_id=user_id).all()

            if len(incomes) == 0:
                return jsonify(TrueReturn('',msg='暂无收入.'))

            res = []
            for income in incomes:

                temp = {
                    'income_money':income.income_price,
                    'income_from':income.from_user,
                    'income_time':income.income_time,
                }
                res.append(temp)
                del temp

            data = {
                'incomes':res
            }

            return jsonify(TrueReturn(data,'请求成功'))

        except:
            return jsonify(FalseReturn('',msg='500,服务器内部错误.'))


