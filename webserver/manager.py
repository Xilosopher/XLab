# -*- coding: utf-8 -*-
#
# Copyright 2017 Xilosopher
#
# Author: Moro JoJo


from webserver.app import create_app


def start_server(host='localhost', port=36728):
    app = create_app('development')
    app.run(host=host, port=port, use_reloader=False, debug=True)


if __name__ == '__main__':
    start_server()
