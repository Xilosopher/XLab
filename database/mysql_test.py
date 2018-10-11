# -*- coding: utf-8 -*-
#
# Copyright 2017 Xilosopher
#
# Author: Moro JoJo


import pymysql
import tushare as ts
import datetime


if __name__ == "__main__":
    print(datetime.datetime.now())
    df = ts.get_tick_data('600848', date='2017-04-10')
    count = len(df)
    print(datetime.datetime.now())

    conn = pymysql.connect(user='liyuhuang', passwd='123456',
                           host='localhost', db='db_tushare', charset='utf8')
    cur = conn.cursor()


    sql_create_tb = "CREATE TABLE tb_tick (c_time varchar(10), c_price float, c_change varchar(10), c_volume int, c_amount int, c_type varchar(10)) ENGINE=InnoDB DEFAULT CHARSET=utf8"

    try:
        sta = cur.execute(sql_create_tb)
        print('result is ', sta)
    except Exception as e:
        print(e)
    else:
        print('ok')

        for index in range(0, count):
            tick = df.iloc(0)[index]
            sql_insert_data = "INSERT INTO tb_tick (c_time,c_price,c_change,c_volume,c_amount,c_type) VALUES ('%s',%f,'%s',%d,%d,'%s')" % \
                 (tick['time'], tick['price'], tick['change'], tick['volume'], tick['amount'], tick['type'])
            print(sql_insert_data)
            sta = cur.execute(sql_insert_data)
            if sta == 1:
                print('Done')
            else:
                print('Failed')

    conn.commit()
    cur.close()
    conn.close()
    print(datetime.datetime.now())
