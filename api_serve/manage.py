#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : classmate Lin.
# @Email   : 406728295@qq.com
# @File    : manage.py
# @Time    : 18-9-27 下午9:37

'''
数据迁移脚本
'''


from app.app import AppFactory
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from app.models.base import db,Base
from app.models.user import Users
from app.models.lesson import Lessons
from app.models.order import Orders
from app.models.price import Price
from app.models.income import UserWallet,UserIncome
from app.models.coupon import Coupon
from app.models.spread import Spread
from app.models.admin import AdminUser

app = AppFactory.create_app()

manager = Manager(app=app)

migrate = Migrate(app,db)

manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manager.run()
