# -*- coding: utf-8 -*-
#
# Copyright 2017 Xilosopher
#
# Author: Moro JoJo


from sqlalchemy import Column, Unicode, Integer, DateTime, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Task(Base):
    __tablename__ = 'tb_task'
    c_task_id = Column(Integer, primary_key=True, nullable=False)
    c_title = Column(Unicode(30), nullable=False)
    c_brief = Column(Unicode(100))
    c_start_date = Column(DateTime())
    c_end_date = Column(DateTime())
    c_finished_date = Column(DateTime())
    c_status = Column(Integer)
    c_agents = Column(Unicode(50))

    def __init__(self, task_id, title, brief, start_date, end_date, finished_date, status, agents):
        self.c_task_id = task_id
        self.c_title = title
        self.c_brief = brief
        self.c_start_date = start_date
        self.c_end_date = end_date
        self.c_finished_date = finished_date
        self.c_status = status
        self.c_agents = agents

engine = create_engine('mysql+pymysql://liyuhuang:123456@localhost:3306/db_webframe?charset=utf8')

DBSession = sessionmaker(bind=engine)

session1 = DBSession()
task_list = session1.query(Task).all()
for i in range(len(task_list)):
    print('Task#%d %s: %s' % (task_list[i].c_task_id, task_list[i].c_title, task_list[i].c_brief))
session1.close()
