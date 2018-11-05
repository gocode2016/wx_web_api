#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : classmate Lin.
# @Email   : 406728295@qq.com
# @File    : income.py
# @Time    : 18-10-3 下午2:34

from flask_admin.contrib.sqla import ModelView

from app.admin.admin import current_user


class IncomeView(ModelView):

    def is_accessible(self):
        return current_user.is_authenticated

    column_display_all_relations = True

    create_modal = True
    edit_modal = True
    can_export = True
    can_create = True

    column_list = [
        'user_id',
        'income_price',
        'from_user',
        'income_time'

    ]

    column_labels = {
        'user_id':'用户编号',
        'income_price':'收入金额',
        'from_user':'收入来源',
        'income_time':'收入时间'
    }

    column_formatters = dict(
        income_price=lambda v,c,m,p: str(m.income_price/100)+' 元',
    )

class WalletView(ModelView):

    def is_accessible(self):
        return current_user.is_authenticated


    column_list = [

        'user_id',
        'not_put_forward',
        'already_preseted',
        'withdraw_cashint',
    ]

    column_labels = {
        'user_id':'用户编号',
        'not_put_forward': '未提现',
        'already_preseted': '已提现',
        'withdraw_cashint': '提现中'
    }

    column_formatters = dict(
        not_put_forward=lambda v, c, m, p: str(m.not_put_forward/100)+' 元', #订单金额
        already_preseted=lambda v,c,m,p: str(m.already_preseted/100)+' 元',
         withdraw_cashint=lambda v,c,m,p: str(m.withdraw_cashint/100)+' 元'
    )


    column_display_all_relations = True

    create_modal = True

    edit_modal = True

    can_export = True

    can_create = True

    can_edit = True

    can_set_page_size = True

    can_delete = True
