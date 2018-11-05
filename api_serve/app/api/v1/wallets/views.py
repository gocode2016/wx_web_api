#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : classmate Lin.
# @Email   : 406728295@qq.com
# @File    : views.py
# @Time    : 18-10-6 下午10:27

'''
获取用户提现详情
'''


from app.libs.redprint import Redprint
from app.forms.api.income import WalletForm
from app.models.income import UserWallet

from flask import jsonify
from app.libs.response import TrueReturn,FalseReturn

api = Redprint('wallet')


class WalletView:

    @staticmethod
    @api.route('',methods=['GET'])
    def wallet_view():

        form = WalletForm.create_api_form()
        form.validate()
        user_id = form.user_id.data

        try:

            user = UserWallet.query.filter_by(user_id=user_id).first()

            if user is None:
                return jsonify(FalseReturn('','暂无该用户信息.'))

            data = {
                "not_cash":user.not_put_forward,
                "is_cash":user.already_preseted,
                "in_cash":user.withdraw_cashint,
            }

            return jsonify(TrueReturn(data,'请求成功.'))

        except:

            return jsonify(FalseReturn('','服务器内部错误:  500'))

