#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : classmate Lin.
# @Email   : 406728295@qq.com
# @File    : user.py
# @Time    : 18-10-3 上午11:34


from flask_admin.form import BaseForm
from wtforms import IntegerField,StringField,PasswordField,ValidationError
from wtforms.validators import DataRequired,Email,Length
from wtforms import Form

from app.models.admin import AdminUser

from werkzeug.security import check_password_hash

class UsersForm(BaseForm):
    '''
    后台显示优学院用户
    '''
    user_id = IntegerField()

    account = StringField()

    password = StringField()

    #真实姓名
    realname = StringField()

    schoolname = StringField()



class LoginForm(Form):
    '''
    后台管理登录验证
    '''


    #账号验证
    account = StringField(validators=[
        DataRequired(),Length(min=2,max=10)
    ])

    #密码验证

    password = PasswordField(validators=[
        DataRequired(),
        Length(min=9,max=20),
    ])


    def validate_login(self):

        '''
        验证账号密码是否正确
        :return:
        '''

        user = self.get_user()
        print(user)

        if user is None:
            raise ValidationError('invalid user.')

        if not check_password_hash(user.password,self.password.data):

            raise ValidationError('invalid password.')





    def get_user(self):
        account = self.account.data

        return AdminUser.query.filter_by(account=account).first()
