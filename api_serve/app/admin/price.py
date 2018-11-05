#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : classmate Lin.
# @Email   : 406728295@qq.com
# @File    : price.py
# @Time    : 18-10-3 下午2:39


from flask_admin.contrib.sqla import ModelView
from app.forms.admin.price import PriceForm

from app.admin.admin import current_user

class PriceView(ModelView):

    def is_accessible(self):
        return current_user.is_authenticated

    form_base_class = PriceForm

    form_columns = [
        'lesson_id',
        'lesson_name',
        'unit_price',
        'all_price'
    ]

    column_labels = {
        'lesson_id':'课程编号',
        'lesson_name':'课程名称',
        'unit_price':'单元价格(元)',
        'all_price':'全册价格(元)'
    }

    #格式化输出
    column_formatters = dict(
        unit_price=lambda v, c, m, p: str(m.unit_price/100)+' 元', #单元价格

        all_price=lambda v, c, m, p: str(m.all_price/100)+' 元',#全册价格
    )



    column_display_all_relations = False



    create_modal = True

    edit_modal = True

    can_export = True

    can_create = True

    can_edit = True

    can_set_page_size = True

    can_delete = True

