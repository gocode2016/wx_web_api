#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : classmate Lin.
# @Email   : 406728295@qq.com
# @File    : spread.py
# @Time    : 18-10-3 下午2:42

from flask_admin.contrib.sqla import ModelView

from app.admin.admin import current_user


class SpreadView(ModelView):

    def is_accessible(self):
        return current_user.is_authenticated

    column_list = [
        'user_id',
        'share_code',
        'higher_upsn',
        'rate_of_pay'
    ]

    column_labels = {
        'user_id':'用户编号',
        'share_code':'分享码',
        'higher_upsn':'上级用户',
        'rate_of_pay':'报酬率'
    }

    column_formatters = dict(
        rate_of_pay = lambda v, c, m, p: str(m.rate_of_pay) + ' %'
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
