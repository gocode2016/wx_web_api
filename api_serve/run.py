#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : classmate Lin.
# @Email   : 406728295@qq.com
# @File    : run.py
# @Time    : 18-9-27 下午9:37


from app.app import AppFactory

from app.models.user import Users,WxUsers
from app.models.order import Orders
from app.models.lesson import Lessons
from app.models.coupon import Coupon
from app.models.income import UserIncome
from app.models.base import db


app = AppFactory.create_app(debug=True)




@app.route('/')
def index():
    order = Orders.query.filter_by(mch_order_id='123456789').first()
    order.pay_status = 1
    Orders.update(Orders)
    return '1'


if __name__ == '__main__':

    app.run(host='0.0.0.0')