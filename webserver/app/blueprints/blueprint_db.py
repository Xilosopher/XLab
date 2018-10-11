# -*- coding: utf-8 -*-
#
# Copyright 2017 Xilosopher
#
# Author: Moro JoJo


from flask import Blueprint, render_template, request, jsonify
from jinja2 import TemplateNotFound

from webserver.app.models.models import TB_DATA


blueprint_db = Blueprint('blueprint_db', __name__, template_folder='templates')


@blueprint_db.route('/db')
def app_index():
    return render_template('db/db_index.html')


@blueprint_db.route('/db/get', methods=['GET'])
def get():
    if not request.args or 'cid' not in request.args:
        return err_to_json('Bad params.')

    get_id = request.args.get('cid')
    try:
        ret_data = TB_DATA.query.filter_by(c_id=get_id).first()
    except Exception as e:
        print(e)
        return err_to_json(str(e))
    else:
        if ret_data is None:
            return data_to_json(data={}, msg='Query result is none.')
        else:
            return data_to_json(data=ret_data.to_json())


@blueprint_db.route('/db/query', methods=['POST'])
def query():
    get_id = request.form.get('cid')
    if get_id is not None:
        try:
            ret_data = TB_DATA.query.filter_by(c_id=get_id).first()
        except Exception as e:
            # print(e)
            return err_to_json(str(e))
        else:
            if ret_data is None:
                return data_to_json(data={}, msg='Query result is none.')
            else:
                return data_to_json(data=ret_data.to_json())
    else:
        return err_to_json('Bad params.')


def err_to_json(err):
    return jsonify({
        'succeed': False,
        'msg': err
    })


def data_to_json(data, msg='Operation succeeded', succeed=True):
    return jsonify({
        'succeed': succeed,
        'msg': msg,
        'data': data
    })
