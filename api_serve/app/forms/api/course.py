#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : classmate Lin.
# @Email   : 406728295@qq.com
# @File    : course.py
# @Time    : 18-10-6 下午6:59

from app.forms.api.base import BaseForm

from wtforms.validators import DataRequired

from wtforms.fields import IntegerField



class CourseForm(BaseForm):

    course_id = IntegerField(validators=[
        DataRequired()
    ])

    user_id = IntegerField(
        validators=[
            DataRequired()
        ]
    )