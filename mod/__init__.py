# -*- coding: utf-8 -*-
#
# Copyright 2017 Xilosopher
#
# Author: Moro JoJo


import copy
from collections import OrderedDict
from utils.logger import mod_log
from utils.mod_helper import import_mod


class ModHandler(object):
    def __init__(self):
        self._env = None
        self._mod_list = list()
        self._mod_dict = OrderedDict()

    def set_env(self, environment):
        self._env = environment
        config = environment.config

        for mod_name in config.mod.__dict__:
            mod_config = getattr(config.mod, mod_name)
            if not mod_config.enabled:
                continue
            self._mod_list.append((mod_name, mod_config))

        for index, (mod_name, user_mod_config) in enumerate(self._mod_list):
            if hasattr(user_mod_config, 'lib'):
                lib_name = user_mod_config.lib
            elif mod_name in MOD_LIST:
                lib_name = 'sys_mod_' + mod_name
            else:
                lib_name = 'mod_' + mod_name
            mod_log.debug("loading mod {}".format(lib_name))
            mod_module = import_mod(lib_name)
            if mod_module is None:
                del self._mod_list[index]
                return
            mod = mod_module.load_mod()

            mod_config = copy.deepcopy(getattr(mod_module, "__config__", {}))
            mod_config.update(user_mod_config)
            setattr(config.mod, mod_name, mod_config)
            self._mod_list[index] = (mod_name, mod_config)
            self._mod_dict[mod_name] = mod

        self._mod_list.sort(key=lambda item: getattr(item[1], "priority", 100))
        environment.mod_dict = self._mod_dict

    def start_up(self):
        for mod_name, mod_config in self._mod_list:
            self._mod_dict[mod_name].start_up(self._env, mod_config)

    def tear_down(self, *args):
        result = {}
        for mod_name, __ in reversed(self._mod_list):
            ret = self._mod_dict[mod_name].tear_down(*args)
            if ret is not None:
                result[mod_name] = ret
        return result


MOD_LIST = [
    'sample'
]


