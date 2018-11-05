#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : classmate Lin.
# @Email   : 406728295@qq.com
# @File    : admin.py
# @Time    : 18-10-5 下午7:51

from flask import url_for,redirect,request



from flask_admin import AdminIndexView
from flask_admin import expose,helpers

from flask_login import current_user,logout_user,login_user

from app.forms.admin.user import LoginForm



class AdminView(AdminIndexView):
    '''管理员视图'''

    @expose('/')
    def index(self):
        '''
        管理未登录则跳转登录页面。
        :return:
        '''
        if not current_user.is_authenticated:
            return redirect(url_for('.login_view'))

        return super(AdminView,self).index()


    @expose('/login',methods=['GET','POST'])
    def login_view(self):

        form = LoginForm(request.form)

        try:
            form.validate()
            form.validate_login()

        except:
            self._template_args['form'] = form
            self._template_args['errors'] = True

            return super(AdminView,self).index()


        if helpers.validate_form_on_submit(form):
            user = form.get_user()
            login_user(user)

        if current_user.is_authenticated:
            return redirect(url_for('.index'))


        self._template_args['form'] = form

        return super(AdminView, self).index()


    @expose('loyout',methods=['GET','POST'])
    def logout_view(self):
        '''
        注销登录跳转首页
        :return:
        '''

        logout_user()

        return redirect(url_for('.index'))