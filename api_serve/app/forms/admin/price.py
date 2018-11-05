#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : classmate Lin.
# @Email   : 406728295@qq.com
# @File    : price.py
# @Time    : 18-10-3 下午3:35



from flask_admin.form import BaseForm
from wtforms import IntegerField,StringField


class PriceForm(BaseForm):

 #   id = IntegerField()

    #课程id
    lesson_id = IntegerField()

    # 课程名称
    lesson_name = StringField()

    #每单元价格
    unit_price = IntegerField()

    #全册价格
    all_price = IntegerField()

