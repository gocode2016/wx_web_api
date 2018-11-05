#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : classmate Lin.
# @Email   : 406728295@qq.com
# @File    : app.py
# @Time    : 18-10-2 上午11:05

'''
app 工厂方法的定义，完成各初始化操作.
'''

from flask import Flask

class AppFactory:
    '''
    仅仅是将方法整合到一个类中.
    '''

    @staticmethod
    def create_app(debug=True):
        '''
        工厂函数,注册需要加载的组件
        '''

        #from app.config.secure import MysqlConf,CsrfConf,REDIS_CONFIG,SECRET_KEY
        from app.config.secure import MysqlConf,CsrfConf,REDIS_CONFIG,SECRET_KEY
        app = Flask(__name__)

        app.config['SECRET_KEY'] = SECRET_KEY

        #加载配置
        AppFactory.register_config(app, [MysqlConf, CsrfConf,REDIS_CONFIG])


        #加载数据库
        AppFactory.register_db(app)

        #增加后台管理模块
        AppFactory.register_admin(app)

        #修改后台显示语言
        AppFactory.register_babelex(app)

        #加载后台管理登录模块
        AppFactory.register_admin_login(app)

        #加载微信模块
        AppFactory.register_weixin(app)

        #加载蓝图
        AppFactory.register_bp(app)

        AppFactory.register_cache(app)

        AppFactory.handler_for_404(app)

        AppFactory.handler_for_405(app)

        return app

    @staticmethod
    def register_config(app,conf_list):

        for conf in conf_list:
            app.config.from_object(conf)


    @staticmethod
    def register_db(app):
        '''
        加载db
        '''
        from app.models.base import db
        from app.models.admin import AdminUser
        db.init_app(app)

        # 创建所有表
        with app.app_context():
            db.create_all()

            user = AdminUser.query.filter_by(account='ly').first()
            if user is None:
                user = AdminUser(account='ly',email='406728295@qq.com',password=AdminUser.hash_password(AdminUser,'123456789'))
                db.session.add(user)
                db.session.commit()


    @staticmethod
    def register_auth(app):
        '''
        加载json token认证模块
        '''

        pass


    @staticmethod
    def register_cache(app):
        '''
        加载缓存
        '''
        from app.libs.cache import cache
        cache.init_app(app)




    @staticmethod
    def register_admin(app):
        '''
        加载后台管理插件
        :param app:
        :return:
        '''

        from app.admin import admin
        admin.init_app(app)


    @staticmethod
    def register_babelex(app):
        from flask_babelex import Babel
        app.config['BABEL_DEFAULT_LOCALE'] = 'zh_CN'
        babel = Babel(app)


    @staticmethod
    def register_admin_login(app):
        '''
        用于加载后台管理登录模块
        :param app:
        :return:
        '''

        from flask_login import LoginManager
        from app.models.admin import AdminUser
        from app.models.base import db
        login_manager = LoginManager()
        login_manager.init_app(app)

        @login_manager.user_loader
        def load_uer(user_id):
            return db.session.query(AdminUser).get(user_id)

    @staticmethod
    def register_bp(app):
        '''
        注册蓝图
        :param app:
        :return:
        '''
        from app.api.v1 import create_blueprint_v1
        app.register_blueprint(create_blueprint_v1(), url_prefix='/v1')


    @staticmethod
    def handler_for_404(app):
        from flask import request,jsonify
        from app.libs.response import FalseReturn

        @app.errorhandler(404)
        def not_found(error=None):


            res = FalseReturn('','Not found:'+request.url)


            return jsonify(res)


    @staticmethod
    def handler_for_405(app):
        from flask import request,jsonify
        from app.libs.response import FalseReturn

        @app.errorhandler(405)
        def not_allowed(error=None):
            res = FalseReturn('',request.method+' is not allowed at '+request.url)
            return jsonify(res)


    @staticmethod
    def register_weixin(app):
        from app.libs.weixin import weixin
        weixin.init_app(app)

if __name__ == "__main__":
    pass