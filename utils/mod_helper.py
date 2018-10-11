# -*- coding: utf-8 -*-
#
# Copyright 2017 Xilosopher
#
# Author: Moro JoJo


from utils.logger import mod_log


def import_mod(mod_name):
    try:
        from importlib import import_module
        return import_module(mod_name)
    except Exception as e:
        mod_log.error("*" * 10)
        mod_log.error("Mod Import Error: ")
        mod_log.error(e)
        mod_log.error("*" * 10)
        return None