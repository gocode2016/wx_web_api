#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : classmate Lin.
# @Email   : 406728295@qq.com
# @File    : views.py
# @Time    : 18-10-5 下午9:49

'''
获取用户课程详情
'''

from flask import request,jsonify

from app.libs.redprint import Redprint
from app.libs.auth import Auth
from app.forms.api.course import CourseForm

from app.libs.ucollege import UCollege
from app.libs.response import TrueReturn,FalseReturn
from app.libs.cache import cache,make_cache_key

api = Redprint('course')


class CourseView:
    '''
    定义视图及其相关操作
    '''

    @staticmethod
    @api.route('',methods=['GET'])
    @cache.cached(timeout=60*10,key_prefix=make_cache_key)
    def course():
        '''
        视图函数
        '''

        result = Auth.identify(Auth,request)

        #未通过token认证返回错误信息
        if result['status'] == False:
            return jsonify(result)

        #表单验证
        form = CourseForm.create_api_form()
        form.validate()

        res_list = UCollege.get_course_detail(form.course_id.data,form.user_id.data)

        if len(res_list) == 0:
            return jsonify(FalseReturn('',msg='用户没有该课程.'))

        data = {
            "course":res_list
        }

        return jsonify(TrueReturn(data,msg='请求成功'))



