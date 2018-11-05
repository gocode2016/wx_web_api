#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : classmate Lin.
# @Email   : 406728295@qq.com
# @File    : ucollege.py
# @Time    : 18-10-6 下午3:11


import requests

from app.libs.utils import md5_encrypt

from app.libs.utils import time2timestamp,get_now_timestamp

class UCollege:

    headers = {
        'Accept-Language': 'CN',
        'User-Agent': 'App ulearning Android',
        'Content-Type': 'application/json;charset=UTF-8',
        'Host': 'apps.ulearning.cn',
    }

    HOST = 'https://apps.ulearning.cn/'

    LOGIN_URL = HOST + 'login'

    GET_COURSE_URL = HOST + "courses/getCourse"

    GET_TIMESTAMP_URL = HOST + 'courses/getTimeStamp'

    GET_UNIT_URL = HOST + 'courses/coursePlan/{}/{}/{}'

    @staticmethod
    def login(account,password):
        sess = requests.Session()
        sess.headers = UCollege.headers

        data = {
            'loginName':account,
            'password':md5_encrypt(password)
        }

        try:
            res = sess.post(UCollege.LOGIN_URL,json=data).json()

        except:
            return None

        if 'code' in res:
            return None


        user_id = res['userID']
        real_name = res['name']
        school_name = res['org']['orgName']

        result = {
            'user_id':user_id,
            'real_name':real_name,
            'school_name':school_name
        }

        try:
            result['tel_num'] = res['tel']
        except:
            result['tel_num'] = ''

        return result


    @staticmethod
    def get_course_list(user_id='',class_id=-1):
        '''
        通过user_id获取课程列表
        :param user_id:
        :param class_id:
        :return:
        '''
        data = {
            'operation': 'getCourse',
            'userID': user_id,
            'classID':class_id
        }

        try:
            res = requests.get(UCollege.GET_COURSE_URL,params=data).json()

        except:
            return None

        return parse_couser_data(res)

    @staticmethod
    def get_course_detail(course_id,user_id,class_id=-1):
        '''通过user_id,course_id 获取课程详情
        '''
        url = UCollege.GET_UNIT_URL.format(course_id, user_id, class_id)
        try:
            res = requests.get(url).json()
        except:
            return None

        return parse_course_unit(res)





def parse_couser_data(course_data):
    '''
    解析未过期的过程，提取需要的数据
    :param course_data:
    :return:
    '''
    res = []
    now_timestamp = get_now_timestamp()

    for course in course_data:

        '''
        过滤已过期的课程。
        '''
        limit_timestamp = time2timestamp(course['limit'])
        if now_timestamp>limit_timestamp:
            continue

        '''
        提取课程名称，课程ID，课程类型，课程截止时间。
        '''
        temp = {
                'course_name':course['title'],
                'course_id':course['courseID'],
                #'courseType':course['courseType'],
                #'limit':course['limit']

        }

        res.append(temp)


    return res



def parse_course_unit(unit_list):
    '''
    解析单元数据，只留下需要的部分
    :param unit_list:
    :return:
    '''
    res = []
    unit_num = 1

    for u in unit_list:
        #print(u)
        temp = {'unit_num':unit_num,'unit_id':u['unitID'],'unit_name':u['unitName']}

        unit_num += 1

        res.append(temp)

    return res



if __name__ == '__main__':
    username = 'hbms17121033'
    password = '17121033'

   # UCollege.login(username,password)
    #result = UCollege.get_course('3908262')
    reslut = UCollege.get_course_detail('7451','3908262')
    print(reslut)