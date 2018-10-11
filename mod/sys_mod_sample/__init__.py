# -*- coding: utf-8 -*-
#
# Copyright 2017 Xilosopher
#
# Author: Moro JoJo


from interface import AbstractMod


class SampleMod(AbstractMod):
    def start_up(self, env, mod_config):
        print(">>> HelloWorldMod.start_up")

    def tear_down(self, success, exception=None):
        print(">>> HelloWorldMod.tear_down")


def load_mod():
    return SampleMod()