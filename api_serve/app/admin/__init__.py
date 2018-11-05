#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : classmate Lin.
# @Email   : 406728295@qq.com
# @File    : __init__.py.py
# @Time    : 18-10-2 上午10:54

from flask_admin import Admin

from app.models.base import db
from app.admin.users import UsersModelView,WxUsersView
from app.models.user import Users,WxUsers

from app.models.lesson import Lessons
from app.admin.lessons import LessonsView

from app.models.income import UserWallet,UserIncome
from app.admin.income import WalletView,IncomeView

from app.models.price import Price
from app.admin.price import PriceView

from app.admin.spread import SpreadView
from app.models.spread import Spread

from app.models.order import Orders
from app.admin.orders import OrdersView

from app.models.coupon import Coupon
from app.admin.coupon import CouponView

from app.admin.admin import AdminView

#复写后台模板，增加登录表单
admin = Admin(name='后台管理',index_view=AdminView(),base_template='base.html')

#admin = Admin(name='后台管理')

#添加优学院用户后台管理
admin.add_view(UsersModelView(Users,db.session,name='优学用户'))

#添加微信用户后台管理
admin.add_view(WxUsersView(WxUsers,db.session,name='微信用户'))


#添加价格管理
admin.add_view(PriceView(Price,db.session,name='代做价格'))

#添加代做课程后台管理
admin.add_view(LessonsView(Lessons,db.session,name='代做课程'))

#添加订单管理
admin.add_view(OrdersView(Orders,db.session,name='用户订单'))

#添加用户钱包和收入后台管理
admin.add_view(WalletView(UserWallet,db.session,name='用户钱包'))

admin.add_view(IncomeView(UserIncome,db.session,name='用户收入'))




#添加用户推广
admin.add_view(SpreadView(Spread,db.session,name='用户推广'))



#添加用户优惠管理
admin.add_view(CouponView(Coupon,db.session,name='用户优惠'))