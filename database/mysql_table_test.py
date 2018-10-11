# -*- coding: utf-8 -*-
#
# Copyright 2017 Xilosopher
#
# Author: Moro JoJo


import pymysql
import numpy as np
import tushare as ts
import datetime

from database.sql_definition import *
from database.db_connection_pool import *

pool = None
conn = None
cur = None


def init_db_connection():
    global conn
    global cur
    if conn is None:
        conn = pymysql.connect(user=USER, passwd=PASSWORD, host=HOST, db=DB_DEV, charset=CHARSET)
        cur = conn.cursor()


def close_db_connection():
    cur.close()
    conn.close()


def get_db_pool():
    global pool
    if pool is None:
        pool = DBConnectionPool(maxconnections=10, dbtype='mysql', config=mysql_config)
    return pool


########################################## Basic Info ############################################
def create_tb_fundamental_basic_info():
    sql_script = sql_create_tb_fundamental_basic_info
    try:
        result = cur.execute(sql_script)
        print('Result of create table "sql_create_tb_fundamental_basic_info" is ', result)
    except Exception as e:
        print('Exception happened while creating table "sql_create_tb_fundamental_basic_info" :\n', e)
    else:
        print('Table "sql_create_tb_fundamental_basic_info" created.')
    conn.commit()


def create_tb_fundamental_basic_info_pool():
    sql_script = sql_create_tb_fundamental_basic_info
    db_conn = get_db_pool().get_connection()
    print(type(db_conn))
    db_cur = db_conn.cursor()
    try:
        result = db_cur.execute(sql_script)
        print('Result of create table "sql_create_tb_fundamental_basic_info" is ', result)
    except Exception as e:
        print('Exception happened while creating table "sql_create_tb_fundamental_basic_info" :\n', e)
    else:
        print('Table "sql_create_tb_fundamental_basic_info" created.')
    db_conn.commit()
    db_cur.close()
    db_conn.close()


def update_tb_fundamental_basic_info():
    print(datetime.datetime.now())
    df = ts.get_stock_basics()
    count = len(df)
    print(datetime.datetime.now())

    for i in range(0, count):
        code = df.index[i]
        info = df.iloc[i]

        sql_script = sql_update_tb_fundamental_basic_info % (
            code, info['name'], info['industry'], info['area'], info['pe'], info['outstanding'],
            info['totals'], info['totalAssets'], info['liquidAssets'], info['fixedAssets'],
            info['reserved'], info['reservedPerShare'], info['esp'], info['bvps'], info['pb'],
            info['timeToMarket'], info['undp'], info['perundp'], info['rev'], info['profit'],
            info['gpr'], info['npr'], info['holders']
        )

        try:
            result = cur.execute(sql_script)
            print('Result of insert records info table "tb_fundamental_basic_info" is ', result)
        except Exception as e:
            print('Exception happened while insert into table "tb_fundamental_basic_info" :\n', e)
        else:
            print('Insert records into "tb_fundamental_basic_info" done.')

    conn.commit()


def update_tb_fundamental_basic_info_pool():
    print(datetime.datetime.now())
    df = ts.get_stock_basics()
    count = len(df)
    print(datetime.datetime.now())

    db_conn = get_db_pool().get_connection()
    db_cur = db_conn.cursor()
    for i in range(0, count):
        code = df.index[i]
        info = df.iloc[i]

        sql_script = sql_update_tb_fundamental_basic_info % (
            code, info['name'], info['industry'], info['area'], info['pe'], info['outstanding'],
            info['totals'], info['totalAssets'], info['liquidAssets'], info['fixedAssets'],
            info['reserved'], info['reservedPerShare'], info['esp'], info['bvps'], info['pb'],
            info['timeToMarket'], info['undp'], info['perundp'], info['rev'], info['profit'],
            info['gpr'], info['npr'], info['holders']
        )

        try:
            result = db_cur.execute(sql_script)
            print('Result of insert records info table "tb_fundamental_basic_info" is ', result)
        except Exception as e:
            print('Exception happened while insert into table "tb_fundamental_basic_info" :\n', e)
        else:
            print('Insert records into "tb_fundamental_basic_info" done.')

    db_conn.commit()
    db_cur.close()
    db_conn.close()


########################################## Report ############################################
def create_tb_fundamental_report():
    sql_script = sql_create_tb_fundamental_report
    try:
        result = cur.execute(sql_script)
        print('Result of create table "sql_create_tb_fundamental_report" is ', result)
    except Exception as e:
        print('Exception happened while creating table "sql_create_tb_fundamental_report" :\n', e)
    else:
        print('Table "sql_create_tb_fundamental_report" created.')
    conn.commit()


def update_tb_fundamental_report(year, quarter):
    report_quarter = '%d0%1d' % (year, quarter)

    print(datetime.datetime.now())
    df = ts.get_report_data(2016, 1)
    df[np.isnan(df['eps'])] = 0
    df[np.isnan(df['eps_yoy'])] = 0
    df[np.isnan(df['bvps'])] = 0
    df[np.isnan(df['roe'])] = 0
    df[np.isnan(df['epcf'])] = 0
    df[np.isnan(df['net_profits'])] = 0
    df[np.isnan(df['profits_yoy'])] = 0

    count = len(df)

    print(datetime.datetime.now())
    for i in range(0, count):
        info = df.iloc[i]
        if info['code'] == 0:
            print('code is 0, info.code = %s, info.name = %s' % (info['code'], info['name']))
            continue

        sql_script = sql_update_tb_fundamental_report % (
            report_quarter, info['code'], info['name'], info['eps'], info['eps_yoy'], info['bvps'], info['roe'],
            info['epcf'], info['net_profits'], info['profits_yoy'], info['distrib'], info['report_date']
        )

        try:
            result = cur.execute(sql_script)
            print('Result of insert records info table "tb_fundamental_basic_info" is ', result)
        except Exception as e:
            print('Exception happened while insert into table "tb_fundamental_basic_info" :\n', e)
        else:
            print('Insert records into "tb_fundamental_basic_info" done.')

    conn.commit()


if __name__ == '__main__':
    # init_db_connection()
    # create_tb_fundamental_basic_info()
    # update_tb_fundamental_basic_info()
    # close_db_connection()

    # create_tb_fundamental_basic_info_pool()
    # update_tb_fundamental_basic_info_pool()

    init_db_connection()
    create_tb_fundamental_report()
    update_tb_fundamental_report(2017, 1)
    close_db_connection()

