#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : classmate Lin.
# @Email   : 406728295@qq.com
# @File    : users.py
# @Time    : 18-10-6 下午5:12

from wtforms.validators import DataRequired
from wtforms.validators import Length,Regexp
from wtforms.fields import StringField,PasswordField
from app.forms.api.base import BaseForm


class LoginForm(BaseForm):

    username = StringField(validators=[
        DataRequired(),
        Length(min=3,max=20),
        Regexp('^[a-zA-Z0-9+$]')
    ])

    password = PasswordField(validators=[DataRequired()])


