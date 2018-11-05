#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : classmate Lin.
# @Email   : 406728295@qq.com
# @File    : order.py
# @Time    : 18-10-9 下午2:13

from app.forms.api.base import BaseForm
from wtforms import StringField,IntegerField,BooleanField
from wtforms.validators import DataRequired

class OrderPayForm(BaseForm):

    #用户id
    user_id = IntegerField(validators=[
        DataRequired()
    ])

    #课程id
    lesson_id = IntegerField(validators=[
        DataRequired()
    ])

    #订单金额,单位是分
    order_mon = IntegerField(validators=[
        DataRequired()])

    #是否全册
    is_all = BooleanField(validators=[
        DataRequired()
    ])


    #开始单元
    start_unit = IntegerField(validators=[
        DataRequired()
    ])

    #结束单元
    end_unit = IntegerField(validators=[
        DataRequired()
    ])

    #代做类型
    do_type = IntegerField(validators=[
        DataRequired()
    ])


class OrderQueryBaseForm(BaseForm):
    #用户的订单查询
    user_id = IntegerField(validators=[
        DataRequired()
    ])

class OrderQueryDetailForm(BaseForm):
    #订单的详情查询
    order_id = StringField(validators=[
        DataRequired()
    ])



#
# class OrderCloseForm(BaseForm):
#     #关闭订单
#     order_id = StringField(validators=[
#         DataRequired()
#     ])
#
#
# class OrderRefundForm(BaseForm):
#     #申请退款
#     order_id = StringField(validators=[
#         DataRequired()
#     ])
#
#
# class OrderRefundQueryForm(BaseForm):
#     #退款查询
#     order_id = StringField(validators=[
#         DataRequired()
#     ])
