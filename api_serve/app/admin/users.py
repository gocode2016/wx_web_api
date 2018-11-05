#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : classmate Lin.
# @Email   : 406728295@qq.com
# @File    : users.py
# @Time    : 18-10-3 上午11:03

from app.libs.utils import timestamp2time

from flask_admin.contrib.sqla import ModelView


from app.admin.admin import current_user

class UsersModelView(ModelView):

    def is_accessible(self):
        return current_user.is_authenticated


    form_columns = [
        'user_id',
        'realname',
        'schoolname',
        'mobile',
        'account',
        'password',
        'login_time'
    ]

    column_labels = {
        'user_id': '用户编号',
        'account': '优学院账号',
        'password': '优学院密码',
        'realname': '姓名',
        'schoolname': '学校',
        'mobile':'电话号码',
        'login_time':'登录时间'
    }

    column_formatters = dict(login_time=lambda v, c, m, p: timestamp2time(m.login_time))

    #column_display_pk = True

    create_modal = True

    edit_modal = True

    can_export = True

    can_create = True

    can_edit = True

    can_set_page_size = True

    can_delete = True






class WxUsersView(ModelView):

    def is_accessible(self):
        return current_user.is_authenticated


    #需要显示的字段列表
    column_list = ['openid','nickname','user_id']

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

    #修改显示列名
    column_labels = dict(openid='微信用户编号', nickname='微信用户昵称',user_id='用户编号')


