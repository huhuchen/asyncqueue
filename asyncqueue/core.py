#!/usr/bin/env python
# -*- coding: utf-8 -*-

from asyncqueue import enqueue

__title__ = "asyncqueue"
__version__ = "0.0.1"
__author__ = "huhuchen"
__license__ = "MIT"
__copyright__ = "Copyright 2012 huhuchen"
__docformat__ = "restructuredtext"


class Queue(object):

    def __init__(self, allowed=list()):
        self._allowed = list(allowed)

    def send(self, message_type, safety=False):
        def _asyn(function):
            def __asyn(*arg, **kwarg):
                res = function(*arg, **kwarg)
                if message_type in self._allowed:
                    enqueue(message_type, res)
                else:
                    if safety:
                        raise UnSupportedMessageType
                    return res
            return __asyn
        return _asyn

class UnSupportedMessageType(Exception):
    "unsupported message type"

