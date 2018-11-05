#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : classmate Lin.
# @Email   : 406728295@qq.com
# @File    : coupon.py
# @Time    : 18-10-3 下午2:48

from flask_admin.contrib.sqla import ModelView
from app.admin.admin import current_user


def show_coupon_status(v,c,m,p):
    if m.coupon_status == 1:
        return '已使用'
    elif m.coupon_status==0:
        return '待使用'
    else:
        return '未知'

class CouponView(ModelView):
    #登录可见
    def is_accessible(self):
        return current_user.is_authenticated


    column_list = [
        'user_id',
        'coupon_code',
        'coupon_money',
        'coupon_status'
    ]

    column_labels = {
        'user_id':'用户编号',
        'coupon_code':'优惠券码',
        'coupon_money':'优惠金额',
        'coupon_status':'券码状态'
    }

    column_formatters = dict(
        coupon_money = lambda v, c, m, p: str(m.coupon_money/100) + ' 元',
        coupon_status=show_coupon_status,
    )

    #自动检测外键
    column_auto_select_related = True

    #显示关联内容
    column_display_all_relations = True

    create_modal = True

    edit_modal = True

    can_export = True

    can_create = True

    can_edit = True

    can_set_page_size = True

    can_delete = True
