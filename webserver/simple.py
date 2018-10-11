# -*- coding: utf-8 -*-
#
# Copyright 2017 Xilosopher
#
# Author: Moro JoJo


from flask import Flask
from flask import request
from flask import abort
from flask import jsonify
from flask import make_response


object_list = []
object_list.append({
    'id':'1',
    'name':'MoroJoJo',
    'detail':'Niubility'
})

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1>'


@app.route('/signin', methods=['GET'])
def sign_in_get():
    return '''<form action="/signin" method="post">
                  <p><input name="username"></p>
                  <p><input name="password" type="password"></p>
                  <p><button type="submit">Sign In</button></p>
                  </form>'''


@app.route('/signin', methods=['POST'])
def sign_in_post():
    # 需要从request对象读取表单内容：
    if request.form['username'] == 'admin' and request.form['password'] == 'password':
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password.</h3>'


@app.route('/app/add_object', methods=['POST'])
def add_object():
    if not request.json or 'id' not in request.json:
        abort(400)
    new_object = {
        'id': request.json['id'],
        'name': request.json['name'],
        'detail': request.json['detail']
    }
    object_list.append(new_object)
    response_obj = {
        'succeed': True,
        'msg': "Operation Succeeded",
        'code': 0
    }
    return jsonify(response_obj)


@app.route('/app/getObject', methods=['POST', 'GET'])
def get_object():
    if not request.args or 'id' not in request.args:
        abort(400)
    # oid = request.args['id']
    # obj = filter(lambda o:o['id'] == oid, object_list)
    # if len(obj) == 0:
    #     abort(400)
    return jsonify({'object':object_list[0]})


if __name__ == '__main__':
    app.run()


