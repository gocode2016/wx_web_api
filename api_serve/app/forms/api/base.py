#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : classmate Lin.
# @Email   : 406728295@qq.com
# @File    : base.py
# @Time    : 18-10-6 下午5:08

from flask_wtf import FlaskForm
from werkzeug.datastructures import MultiDict
from flask import request
from app.libs.errors import FormError
import json


class BaseForm(FlaskForm):

    @classmethod
    def create_api_form(cls, obj=None):
        '''
        将参数统一转换成字典.
        :param obj:
        :return:
        '''
        if request.method == 'GET':
            data = request.args.to_dict()
        else:
            data = request.get_json()

        formdata = MultiDict(data)
        form = cls(formdata=formdata, obj=obj)
        form._obj = obj

        if not form.validate():
            raise FormError(form)

        return form

    def _validate_obj(self, key, value):
        obj = getattr(self, '_obj', None)
        return obj and getattr(obj, key) == value