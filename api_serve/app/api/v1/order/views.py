#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : classmate Lin.
# @Email   : 406728295@qq.com
# @File    : views.py
# @Time    : 18-10-5 下午10:31

'''
用户下单,用户退款，订单查询
'''

from flask import request,jsonify

from app.libs.response import FalseReturn,TrueReturn
from app.forms.api.order import OrderPayForm,OrderQueryBaseForm,OrderQueryDetailForm

from app.libs.redprint import Redprint

from app.libs.utils import general_mch_order_id,general_pay_body

from app.models.user import WxUsers
from app.models.order import Orders
from app.models.lesson import Lessons

from app.libs.weixin import weixin

from weixin import WeixinError


api = Redprint('order')


class OrderView:

    @staticmethod
    @api.route('pay',methods=['POST'])
    def order_pay_view():
        form = OrderPayForm.create_api_form()
        form.validate()

        #用户编号
        user_id = form.user_id.data
        #订单金额
        total_fee = form.order_mon

        #查询用户是否存在
        user = WxUsers.query.filter_by(user_id=user_id).first()
        if not user:
            return jsonify(FalseReturn('','用户不存在.'))

        openid = user.openid
        pay_body = general_pay_body()
        out_trade_no = general_mch_order_id() #生成订单号


        try:
            raw = weixin.pay.jsapi(openid,pay_body,out_trade_no,total_fee)
            status = add_to_order_db(out_trade_no,total_fee,user_id)
            if not status:
                return jsonify(FalseReturn('','请求失败.'))

            status = add_to_lesson_db(form,out_trade_no)
            if not status:
                return jsonify(FalseReturn('','请求失败'))

            return jsonify(TrueReturn(raw,'请求成功.'))


        except WeixinError as e:
            return jsonify(FalseReturn('',e))


    @staticmethod
    @api.route('notify')
    def notify():
        data = weixin.to_dict(request.data)
        if not weixin.check(data):
            return weixin.reply('签名验证失败',False)

        result_code = data['result_code']
        if result_code == 'FAIL': #SUCCESS/FAIL
            try:
                del_lesson_from_db(mch_order_id=data['out_trade_no'])
                del_order_from_db(mch_order_id=['out_trade_no'])
            except:
                pass
            return weixin.reply('fail',False)

        #支付成功更新订单状态
        update_order(mch_order_id=data['out_trade_no'])

        return weixin.reply("OK",True)


    @staticmethod
    @api.route('QueryBase',methods=['GET'])
    def query_base_view():
        '''获取用户所有订单'''
        form = OrderQueryBaseForm.create_api_form()
        form.validate()
        res = {'orders': []}
        try:
            orders = Orders.query.filter_by(user_id=form.user_id.data).all()
            if len(orders) == 0:
                return FalseReturn('','暂无该用户的订单信息')
            for ods in orders:
                temp = {'order_id':orders.mch_order_id,"pay_status":ods.pay_status,"order_price":ods.order_price}
                res['orders'].append(temp)
                del temp
        except:
            return jsonify(FalseReturn('','服务器内部错误'))

        return jsonify(TrueReturn(res,'请求成功'))


    @staticmethod
    @api.route('QueryDetail',methods=['GET'])
    def query_detail_view():
        '''查询订单的详细信息'''
        form = OrderQueryDetailForm.create_api_form()
        form.validate()

        try:
            lesson = Lessons.query.filter_by(mch_order_id=form.order_id.data).first()
            if lesson == None:
                return jsonify(FalseReturn('','暂无该订单信息'))

            res = {
                'mch_id':lesson.mch_order_id,
                'is_ok':lesson.is_ok,
            }

        except:
            return jsonify(FalseReturn('','服务器内部错误.'))

        return jsonify(TrueReturn(res,'请求成功.'))



def add_to_lesson_db(form,mch_order_id):
    '''将代做课程写入数据库'''
    lesson = Lessons.query.filter_by(mch_order_id=mch_order_id).first()
    if lesson:
        return False

    user_id = form.user_id #用户编号

    lesson_id = form.lesson_id #课程编号

    is_all = form.is_all #是否全册

    start_unit = form.start_unit #开始单元

    end_unit = form.end_unit    #结束单元

    do_type = form.do_type #代做周期类型

    try:

        lesson = Lessons(user_id=user_id,mch_order_id=mch_order_id,lesson_id=lesson_id,
                     is_all=is_all,start_unit=start_unit,end_unit=end_unit,do_time_type=do_type)

        Lessons.add(Lessons,lesson)

    except:

        return False

    return True



def add_to_order_db(mch_order_id,total_fee,user_id):
    '''将订单写入数据库'''
    order = Orders.query.filter_by(mch_order_id=mch_order_id).first()
    if order:
        return False

    pay_status = 0
    order_status = 0

    try:
        order = Orders(mch_order_id=mch_order_id,user_id=user_id,order_price=total_fee,
                   pay_status=pay_status,order_status=order_status)

        Orders.add(Orders,order)

        return True

    except:

        return False



def del_lesson_from_db(mch_order_id):
    try:
        '''删除代做课程'''
        lesson = Lessons.query.filter_by(mch_order_id=mch_order_id).first()
        Lessons.delete(Lessons,lesson)
        return True

    except:

        return False


def del_order_from_db(mch_order_id):
    '''删除订单'''
    try:
        order = Orders.query.filter_by(mch_order_id=mch_order_id).first()
        Orders.delete(Orders,order)
        return True
    except:
        return False


def update_order(mch_order_id):
    '''支付成功更新订单状态'''
    try:
        order = Orders.query.filter_by(mch_order_id=mch_order_id).first()
        order.pay_status = 1
        Orders.update(Orders)
        return True

    except:

        return False

