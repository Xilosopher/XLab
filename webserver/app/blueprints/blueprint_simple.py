# -*- coding: utf-8 -*-
#
# Copyright 2017 Xilosopher
#
# Author: Moro JoJo


from flask import Blueprint, render_template
from jinja2 import TemplateNotFound


blueprint_simple = Blueprint('blueprint_simple', __name__, template_folder='templates')


@blueprint_simple.route('/')
def home():
    return render_template('simple/index.html')


@blueprint_simple.route('/<page>')
def show(page):
    try:
        return render_template('simple/page%s.html' % page)
    except TemplateNotFound:
        return render_template('errors/404.html')