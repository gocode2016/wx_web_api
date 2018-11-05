#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : classmate Lin.
# @Email   : 406728295@qq.com
# @File    : orders.py
# @Time    : 18-10-3 下午2:01



from flask_admin.contrib.sqla import ModelView

from app.admin.admin import current_user


def show_pay_status(v,c,m,p):
    if m.pay_status == 1:
        return '已支付'
    elif m.pay_status == 0:
        return '未支付'

    else:
        return '未知'


def show_order_status(v,c,m,p):
    if m.order_status == 1:
        return '已完成'
    elif m.order_status == 0:
        return '未完成'
    else:
        return '未知'

class OrdersView(ModelView):

    def is_accessible(self):
        return current_user.is_authenticated

    create_modal = True

    edit_modal = True

    can_export = True

    can_create = True

    can_edit = True

    can_set_page_size = True

    can_delete = True

    column_list = [
        'mch_order_id',
        'wx_order_id',
        'user_id',
        # 'lesson_id',
        'order_price',
        'pay_status',
        'order_status',
        'create_time',
        'update_time'
    ]


    column_labels = {
        'mch_order_id':'商户订单编号',
        'wx_order_id':'微信订单编号',
        'user_id':'用户编号',
        # 'lesson_id':'课程编号',
        'pay_status':'支付状态',
        'order_status':'订单状态',
        'order_price':'订单金额',
        'create_time':'创建时间',
        'update_time':'修改时间'
    }


    column_formatters = dict(
        order_price=lambda v, c, m, p: str(m.order_price/100)+' 元', #订单金额
        order_status=show_order_status,
        pay_status = show_pay_status
    )


