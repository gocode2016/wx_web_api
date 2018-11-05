#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : classmate Lin.
# @Email   : 406728295@qq.com
# @File    : lessons.py
# @Time    : 18-10-3 下午2:28

'''
用户下单后的课程
'''

from flask_admin.contrib.sqla import ModelView
from app.admin.admin import current_user


def show_do_type(v, c, m, p):
    if m.do_time_type == 0:
        return '一天一单元'
    elif m.do_time_type == 1:
        return '一周一单元'
    elif m.do_time_type == 2:
        return '三天一单元'


def show_isall(v,c,m,p):
    if m.is_all == True:
        return '是'
    else:
        return '否'


def show_isok(v,c,m,p):
    if m.is_ok == True:
        return '是'
    else:
        return '否'


class LessonsView(ModelView):

    def is_accessible(self):
        return current_user.is_authenticated

    column_list = [
    'user_id',
   # 'wx_order_id',
    'mch_order_id',
    'lesson_id',
    'is_all',
    'start_unit',
    'end_unit',
    'update_time',
    'do_count' ,
    'do_time_type',
    'is_ok'
    ]


    column_labels = {
       # 'wx_order_id':"微信订单编号",
        'mch_order_id':"商户订单编号",
        'user_id':'用户编号',
        'lesson_id':'课程编号',
        'is_all':'是否全册',
        'start_unit':'开始单元',
        'end_unit':'结束单元',
        'update_time':'近期代做时间',
        'do_count':'剩余代做次数',
        'do_time_type':'代做周期类型',
        'is_ok':'是否完成'
    }


    column_formatters = dict(
        do_time_type = show_do_type,
        is_all = show_isall,
        is_ok = show_isok,
    )



    column_display_all_relations = True

    create_modal = True

    edit_modal = True

    can_export = True

    can_create = True

    can_edit = True

    can_set_page_size = True

    can_delete = True



