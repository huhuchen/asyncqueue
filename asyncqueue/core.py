#!/usr/bin/env python
# -*- coding: utf-8 -*-

from asyncqueue._redis import Redis

__title__ = "asyncqueue"
__version__ = "0.0.1"
__author__ = "huhuchen"
__license__ = "MIT"
__copyright__ = "Copyright 2012 huhuchen"
__docformat__ = "restructuredtext"


class Queue(object):

    def __init__(self, allowed=list(), redis_host="localhost", redis_port=6379):
        self._allowed = list(allowed)
        self._redis = Redis(redis_host, redis_port)

    def _check_valid(self, _type, content):
        if _type in self._allowed and content:
            return True
        elif _type not in self._allowed:
            raise UnSupportedMessageType
        elif not content:
            raise WrongMessageContent

    def enqueue(self, message_type, safety=True):
        def _enqueue(function):
            def __enqueue(*arg, **kwarg):
                res = function(*arg, **kwarg)
                if safety:
                    self._check_valid(message_type, res)
                    self._redis.enqueue(message_type, res)
                else:
                    try:
                        self._check_valid(message_type, res)
                        self._redis.enqueue(message_type, res)
                    except:
                        pass
                return res
            return __enqueue
        return _enqueue

    def dequeue(self, qname):
        return self._redis.dequeue(qname)

class UnSupportedMessageType(Exception):
    "unsupported message type"

class WrongMessageContent(Exception):
    "wrong message content"
