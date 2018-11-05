#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : classmate Lin.
# @Email   : 406728295@qq.com
# @File    : views.py
# @Time    : 18-10-5 下午10:25

'''
普通用户登录
'''
'''
登录返回 用户编号，用户姓名，学校名称，课程列表，token
'''

from flask import request,jsonify


from app.libs.redprint import Redprint
from app.libs.auth import Auth
from app.libs.response import FalseReturn,TrueReturn



from app.forms.api.users import LoginForm

from random import randint

api = Redprint('login')




class LoginView:
    '''
    用户登录视图及其相关操作的定义
    '''

    @staticmethod
    @api.route('',methods=['POST'])
    def login_view():

        form = LoginForm().create_api_form()

        form.validate()

        username = form.username.data
        password = form.password.data


        if not username or not password:
            return jsonify(FalseReturn('','用户名和密码不能为空.'))


        result = Auth.authenticate(Auth,username,password)




        return jsonify(result)


