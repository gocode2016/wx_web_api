#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : classmate Lin.
# @Email   : 406728295@qq.com
# @File    : weixin.py
# @Time    : 18-10-9 下午1:51

from app.forms.api.base import BaseForm
from wtforms import StringField,IntegerField
from wtforms.validators import DataRequired

class WxLoginForm(BaseForm):

    code = StringField(validators=[
        DataRequired()
    ])

    user_id = IntegerField(validators=[DataRequired()])