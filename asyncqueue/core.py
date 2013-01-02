#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .job import Job
from ._redis import Redis

__title__ = "asyncqueue"
__version__ = "0.0.1"
__author__ = "huhuchen"
__license__ = "MIT"
__copyright__ = "Copyright 2012 huhuchen"
__docformat__ = "restructuredtext"


class Queue(object):

    redis_queue_namespace_prefix = "asyncqueue:"

    def __init__(self, name, redis_host="localhost", redis_port=6379):
        self._connection = Redis(redis_host, redis_port)
        self._key = None
        self._name = name

    @property
    def key(self):
        self._key = "%s%s" % (self.redis_queue_namespace_prefix, self._name)
        return self._key

    def __call__(self):
        def _func(function):
            def __func(*arg, **kwarg):
                job = Job.create(function, arg, kwarg)
                self.enqueue_job(job)

            function.delay = __func
            return function
        return _func

    def enqueue_job(self, job):
        self._connection.enqueue(self.key, job._data)

    def dequeue_job(self):
        data = self._connection.dequeue(self.key)
        if data:
            return Job.fetch(data)

    def worker(self):
        job = self.dequeue_job()
        if job:
            return job.perform()
