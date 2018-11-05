#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : classmate Lin.
# @Email   : 406728295@qq.com
# @File    : income.py
# @Time    : 18-10-7 下午4:47

from app.forms.api.base import BaseForm
from wtforms.fields import IntegerField
from wtforms.validators import DataRequired

class IncomeForm(BaseForm):

    user_id = IntegerField(validators=[
        DataRequired()
    ])


class WalletForm(BaseForm):

    user_id = IntegerField(validators=[
        DataRequired()
    ])
