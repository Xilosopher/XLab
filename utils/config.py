# -*- coding: utf-8 -*-
#
# Copyright 2017 Xilosopher
#
# Author: Moro JoJo


import os
import json
from utils.logger import framework_log


def get_config_path():
    os_path = os.getcwd()
    return os_path + '/config/config.json'


def load_config(config_path):
    if config_path is None:
        return {}
    if not os.path.exists(config_path):
        framework_log.error("config.json not found in {config_path}").format(config_path)
        return False
    with open(config_path) as json_file:
        config = json.load(json_file)
        return config

