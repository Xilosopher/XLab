# -*- coding: utf-8 -*-
#
# Copyright 2017 Xilosopher
#
# author: Moro JoJo


import abc
from six import with_metaclass


class AbstractMod(with_metaclass(abc.ABCMeta)):
    """
    扩展模块接口。
    """
    @abc.abstractmethod
    def start_up(self, env, mod_config):
        """
        Lab 在系统启动时会调用此接口；在此接口中，可以通过调用 ``env`` 的相应方法来覆盖系统默认组件。

        :param env: 系统环境
        :type env: :class:`~Environment`
        :param mod_config: 模块配置参数
        """
        raise NotImplementedError

    def tear_down(self, code, exception=None):
        """
        Lab 在系统退出前会调用此接口。

        :param code: 退出代码
        :type code: rqalpha.const.EXIT_CODE
        :param exception: 如果在策略执行过程中出现错误，此对象为相应的异常对象
        """
        raise NotImplementedError