# encoding: utf-8


"""
@author: Xilosopher
@contact: liyuhuangjojo@163.com
@software: PyCharm
@file: mongodb_test.py
@time: 2018/8/16 16:00
"""


import pymongo


client = pymongo.MongoClient(host='localhost', port=27017)

db = client['test']
collection = db['member']

for doc in collection.find():
    print(doc)



 
