# -*- coding: utf-8 -*-
#
# Copyright 2017 Xilosopher
#
# Author: Moro JoJo


import os
import logging
from utils.common import get_project_root


'''
日志工具模块
'''


__all__ = ['dm_log']


DATA_MGR_LOG = 0
TEST_BACK_LOG = 1

LOG_PATH = '%s/logs' % get_project_root()


def singleton(cls, *args, **kw):
    instances = {}
    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return _singleton


@singleton
class FrameworkLogger(logging.Logger):
    '''
    frame的日志类
    '''
    def __init__(self):
        logging.Logger.__init__(self, name='framework', level=logging.DEBUG)

        formatter = logging.Formatter("[%(asctime)s] %(name)s [%(levelname)s] %(filename)s LINE %(lineno)d:  %(message)s")
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        self.addHandler(stream_handler)

        file_handler = logging.FileHandler(self.get_log_path())
        file_handler.setFormatter(formatter)
        self.addHandler(file_handler)

    def get_log_path(self):
        path = LOG_PATH
        if not os.path.exists(path):
            os.makedirs(path)
        return '%s/framework.log' % path

framework_log = FrameworkLogger()


@singleton
class ModLogger(logging.Logger):
    '''
    mod的日志类
    '''
    def __init__(self):
        logging.Logger.__init__(self, name='mod', level=logging.DEBUG)

        formatter = logging.Formatter("[%(asctime)s] %(name)s [%(levelname)s] %(filename)s LINE %(lineno)d:  %(message)s")
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        self.addHandler(stream_handler)

        file_handler = logging.FileHandler(self.get_log_path())
        file_handler.setFormatter(formatter)
        self.addHandler(file_handler)

    def get_log_path(self):
        path = LOG_PATH
        if not os.path.exists(path):
            os.makedirs(path)
        return '%s/mod.log' % path

mod_log = ModLogger()


@singleton
class DMLogger(logging.Logger):
    '''
    data_manager的日志类
    '''
    def __init__(self):
        logging.Logger.__init__(self, name='data_manager', level=logging.DEBUG)

        formatter = logging.Formatter("[%(asctime)s] %(name)s [%(levelname)s] %(filename)s LINE %(lineno)d:  %(message)s")
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        self.addHandler(stream_handler)

        file_handler = logging.FileHandler(self.get_log_path())
        file_handler.setFormatter(formatter)
        self.addHandler(file_handler)

    def get_log_path(self):
        path = LOG_PATH
        if not os.path.exists(path):
            os.makedirs(path)
        return '%s/data_manager.log' % path

dm_log = DMLogger()


@singleton
class SimulatorLogger(logging.Logger):
    '''
    simulator的日志类
    '''
    def __init__(self):
        logging.Logger.__init__(self, name='simulator', level=logging.DEBUG)

        formatter = logging.Formatter("[%(asctime)s] %(name)s [%(levelname)s] %(filename)s LINE %(lineno)d:  %(message)s")
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        self.addHandler(stream_handler)

        file_handler = logging.FileHandler(self.get_log_path())
        file_handler.setFormatter(formatter)
        self.addHandler(file_handler)

    def get_log_path(self):
        path = LOG_PATH
        if not os.path.exists(path):
            os.makedirs(path)
        return '%s/simulator.log' % path

simulator_log = SimulatorLogger()

@singleton
class WebFrameLogger(logging.Logger):
    '''
    web framework的日志类
    '''
    def __init__(self):
        logging.Logger.__init__(self, name='webframe', level=logging.DEBUG)

        formatter = logging.Formatter("[%(asctime)s] %(name)s [%(levelname)s] %(filename)s LINE %(lineno)d:  %(message)s")
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        self.addHandler(stream_handler)

        file_handler = logging.FileHandler(self.get_log_path())
        file_handler.setFormatter(formatter)
        self.addHandler(file_handler)

    def get_log_path(self):
        path = LOG_PATH
        if not os.path.exists(path):
            os.makedirs(path)
        return '%s/webframe.log' % path

webframe_log = WebFrameLogger()