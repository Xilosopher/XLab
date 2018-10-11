# -*- coding: utf-8 -*-
#
# Copyright 2017 Xilosopher
#
# Author: Moro JoJo


from webserver.app import db


class TB_DATA(db.Model):
    __tablename__ = 'tb_data'
    c_id = db.Column(db.String(10), nullable=False, primary_key=True)
    c_name = db.Column(db.Unicode(50), nullable=False)
    c_description = db.Column(db.Unicode(100), nullable=False)
    c_create_time = db.Column(db.DateTime)
    c_update_time = db.Column(db.DateTime)

    def to_json(self):
        json_comment = {
            'c_id': self.c_id,
            'c_name': self.c_name,
            'c_description': self.c_description,
            'c_create_time': self.c_create_time,
            'c_update_time': self.c_update_time
        }
        return json_comment

    def __repr__(self):
        return '<Data %s>' % self.c_name
