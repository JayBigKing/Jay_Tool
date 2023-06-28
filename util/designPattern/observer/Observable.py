#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

"""
@Project : DUAVTracking
@File    : Observable.py
@Author  : jay.zhu
@Time    : 2023/6/28 20:19
"""
from Jay_Tool.util.designPattern.observer.Observer import Observer


def Observable(cls):
    class ObservableCls(cls):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self._ObservableObserverList = []
            self._ObservableChangeFlag = False

        def addObserver(self, observer):
            if isinstance(observer, Observer) is False:
                print('the input observer is not subclass of Observer, it might be cause some wrong')
            self._ObservableObserverList.append(observer)

        def notifyObservers(self):
            if self._ObservableChangeFlag is True:
                for observer in self._ObservableObserverList:
                    observer.update(observable=self)

            self._ObservableChangeFlag = False

        def setChange(self):
            self._ObservableChangeFlag = True

    return ObservableCls


# class Observable:
#     def __init__(self):
#         self._ObservableObserverList = []
#         self._ObservableChangeFlag = False
#
#     def addObserver(self, observer):
#         if isinstance(observer, Observer) is False:
#             print('the input observer is not subclass of Observer, it might be cause some wrong')
#         self._ObservableObserverList.append(observer)
#
#     def notifyObservers(self):
#         if self._ObservableChangeFlag is True:
#             for observer in self._ObservableObserverList:
#                 observer.update(observable=self)
#
#         self._ObservableChangeFlag = False
#
#     def setChange(self):
#         self._ObservableChangeFlag = True




