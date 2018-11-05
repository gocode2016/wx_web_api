#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : classmate Lin.
# @Email   : 406728295@qq.com
# @File    : coupon.py
# @Time    : 18-10-7 下午3:25


from app.forms.api.base import BaseForm

from wtforms.validators import DataRequired,ValidationError
from wtforms import IntegerField


class CouponForm(BaseForm):

    user_id = IntegerField(validators=[
        DataRequired()
    ])