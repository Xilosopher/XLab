# -*- coding: utf-8 -*-
#
# Copyright 2017 Xilosopher
#
# Author: Moro JoJo


from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy

from webserver.app.config import config


bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()


def create_app(config_name):
    application = Flask(__name__)
    application.config.from_object(config[config_name])
    config[config_name].init_app(application)

    bootstrap.init_app(application)
    mail.init_app(application)
    moment.init_app(application)
    db.init_app(application)

    from webserver.app.blueprints.blueprint_simple import blueprint_simple
    from webserver.app.blueprints.blueprint_app import blueprint_app
    from webserver.app.blueprints.blueprint_db import blueprint_db

    application.register_blueprint(blueprint_simple)
    application.register_blueprint(blueprint_app)
    application.register_blueprint(blueprint_db)

    return application
