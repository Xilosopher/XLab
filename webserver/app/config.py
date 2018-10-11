# -*- coding: utf-8 -*-
#
# Copyright 2017 Xilosopher
#
# Author: Moro JoJo


import os


base_dir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = 'hard to guest string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    host = 'localhost'
    port = 36728

    @staticmethod
    def init_app(cls):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://liyuhuang:123456@localhost:3306/db_dev?charset=utf8'

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)


class TestConfig(Config):
    TEST = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://liyuhuang:123456@localhost:3306/db_test?charset=utf8'

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)


class ProductionConfig(Config):
    PRODUCTION = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://liyuhuang:123456@localhost:3306/db_production?charset=utf8'

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)


config = {
    'development': DevelopmentConfig,
    'test': TestConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

