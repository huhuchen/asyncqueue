#!/usr/bin/env python
# -*- coding: utf-8 -*-

from asyncqueue.job import Job
from asyncqueue._redis import Redis

__title__ = "asyncqueue"
__version__ = "0.0.1"
__author__ = "huhuchen"
__license__ = "MIT"
__copyright__ = "Copyright 2012 huhuchen"
__docformat__ = "restructuredtext"


class Queue(object):

    redis_queue_namespace_prefix = "asyncqueue"

    def __init__(self, allowed=list(), redis_host="localhost", redis_port=6379):
        self._allowed = list(allowed)
        self._connection = Redis(redis_host, redis_port)
        self._key = None
        self._message_type = None

    def _check_type_valid(self, _type):
        if _type in self._allowed:
            return True
        elif _type not in self._allowed:
            raise UnSupportedMessageType
        return False

    @property
    def key(self):
        self._key = "%s:%s" % (self.redis_queue_namespace_prefix, self._message_type)
        return self._key

    def __call__(self, message_type):
        self._message_type = message_type
        def _func(function):
            def __func(*arg, **kwarg):
                job = Job.create(function, arg, kwarg)
                self.enqueue_job(job)
            function.delay = __func
            return function
        return _func

    def enqueue_job(self, job):
        print "key", self.key
        self._connection.enqueue(self.key, job._data)

    def dequeue_job(self, qname):
        key = "%s:%s" % (self.redis_queue_namespace_prefix, qname)
        pickle_data = self._connection.dequeue(key)
        if pickle_data:
            return Job.fetch(pickle_data)

    def worker(self, qname):
        job = self.dequeue_job(qname)
        if job:
            return job.perform()




class UnSupportedMessageType(Exception):
    "unsupported message type"

class WrongMessageContent(Exception):
    "wrong message content"
