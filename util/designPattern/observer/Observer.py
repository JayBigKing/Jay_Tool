#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

"""
@Project : DUAVTracking
@File    : Observer.py
@Author  : jay.zhu
@Time    : 2023/6/28 20:19
"""
from abc import ABC, abstractmethod

class Observer(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def update(self, observable=None, arg=None, **kwargs):
        pass
