#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : classmate Lin.
# @Email   : 406728295@qq.com
# @File    : auth.py
# @Time    : 18-10-6 下午12:39

'''
token 认证模块

先从本身数据库查找用户是否存在，存在则直接返回用户信息和课程列表及token。
不存在则用账号密码去登录优学院,将用户信息入库。





'''


import jwt,datetime,time
from flask import jsonify,request
from app.models.user import Users

from app.config.secure import SECRET_KEY
from app.libs.response import TrueReturn,FalseReturn

from app.libs.ucollege import UCollege
from random import randint

from app.models.base import db
from app.models.user import Users
from app.models.spread import Spread


class Auth:

    @staticmethod
    def encode_auth_token(user_id,login_time):
        '''
        生成token。
        :param user_id: int
        :param login_time:  int(timestamp)
        :return:
        '''

        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0,minutes=10),#过期时间
                'iat': datetime.datetime.utcnow(),#签发时间
                'iss':'classmate Lin',  #签发者
                'data': {
                    'id':user_id,
                    'login_time':login_time
                }
            }

            return jwt.encode(
                payload,
                SECRET_KEY,
                algorithm='HS256'

            )


        except Exception as e:

            return e



    @staticmethod
    def decode_auth_token(auth_token):
        '''
        验证token
        :param auth_token:
        :return: integer|string
        '''

        try:

            payload = jwt.decode(auth_token,SECRET_KEY,options={'verify_exp': False})

            if 'data' in payload and 'id' in payload['data']:
                return payload

            else:
                raise jwt.InvalidTokenError

        except jwt.ExpiredSignatureError:
            return 'Token 过期.'

        except jwt.InvalidTokenError:
            return 'Token 无效.'


    def authenticate(self, username, password):
        """

        用户登录，登录成功返回token，写将登录时间写入数据库；登录失败返回失败原因.
        用户登录先从数据库找，如果数据库中不存在,则用该账号去登录优学院.
        :param password:
        :return: json
        """
        userInfo = Users.query.filter_by(account=username).first()

        if (userInfo is None):
            #登录优学院获取用户信息
            res = UCollege.login(account=username,password=password)

            #优学院登录也失败。说明用户不存在
            if res == None:
                return FalseReturn('', '账号或者密码错误.')

            else:
                #j将用户信息写入数据库,并返回token.
                login_time = int(time.time())

                user_id = add_user_to_db(res,username,password,login_time)

                try:#增加上级用户
                    add_up_user(user_id,request)
                except:
                    pass

                token = self.encode_auth_token(user_id, login_time)


                res['token'] = token.decode()
                res['course'] = UCollege.get_course_list(user_id)

                #电话号码不必返回到前端
                del res['tel_num']


                return TrueReturn(res,'登录成功')

        else:
            #数据库存在该用户并且密码正确，返回用户信息，并返回课程信息.
            if userInfo.password == password:

                login_time = int(time.time())
                userInfo.login_time = login_time
                Users.update(Users)

                token = self.encode_auth_token(userInfo.user_id, login_time)

                data = {
                    'user_id':userInfo.user_id,
                    'real_name':userInfo.realname,
                    'school_name':userInfo.schoolname,
                    'token':token.decode(),
                    'course':UCollege.get_course_list(userInfo.user_id)
                }

                return TrueReturn(data, '登录成功')

            else:

                return FalseReturn('', '密码不正确')

    def identify(self, request):
        """
        用户鉴权
        :return: list
        """
        auth_token = request.headers.get('Authorization')

        if auth_token:
            payload = self.decode_auth_token(auth_token)
            if not isinstance(payload, str):
                user = Users.query.filter_by(user_id=payload['data']['id']).first()

                if (user is None):
                    result = FalseReturn('', '找不到该用户信息')
                else:
                    if (user.login_time == payload['data']['login_time']):
                        result = TrueReturn(user.user_id, '请求成功')
                    else:
                        result = FalseReturn('', 'Token已更改，请重新登录获取')
            else:
                result = FalseReturn('', payload)

        else:

            result = FalseReturn('', '没有提供Token信息.')



        return result




def add_user_to_db(res,username,password,login_time):

    user = Users()
    user.user_id = res['user_id']
    user.account = username,
    user.realname = res['real_name']
    user.password = password
    user.schoolname = res['school_name']
    user.login_time = login_time
    user.mobile = res['tel_num']
    Users.add(Users, user)

    return user.user_id


def add_up_user(user_id, request):
    share_code = request.json.get('code')
    print(share_code)
    if share_code is None or type(share_code) != int:
        up_user_id = -1

    else:

        user_spread = Spread.query.filter_by(share_code=share_code).first()
        if user_spread is None:
            up_user_id = -1
        else:
            up_user_id = user_spread.user_id

    try:

        spread = Spread(user_id=user_id, share_code=randint(100000,999999), higher_upsn=up_user_id, rate_of_pay=5)
        db.session.add(spread)
        db.session.commit()

    except:
        return False

    return True