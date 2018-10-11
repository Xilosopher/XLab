# -*- coding: utf-8 -*-
#
# Copyright 2017 Xilosopher
#
# Author: Moro JoJo


from flask import Blueprint, render_template
from jinja2 import TemplateNotFound


blueprint_app = Blueprint('blueprint_app', __name__, template_folder='templates')


@blueprint_app.route('/app', methods=['POST', 'GET'])
def app_index():
    return render_template('app/app_index.html')


@blueprint_app.route('/app/<app>')
def show(app):
    try:
        return render_template('app/app_%s.html' % app)
    except TemplateNotFound:
        return render_template('errors/404.html')
