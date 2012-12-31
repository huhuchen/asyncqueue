#!/usr/bin/env python
# -*- coding: utf-8 -*-

import inspect
import importlib
from pickle import dumps, loads

class Job(object):

    @classmethod
    def create(cls, func, args=None, kwargs=None):
        if args is None:
            args = ()
        if kwargs is None:
            kwargs = {}
        assert isinstance(args, tuple), "%r is not a valid args list" % (args, )
        assert isinstance(kwargs, dict), "%r is not a valid kwargs dict" % (kwargs, )
        job = cls()
        if inspect.isfunction(func):
            job._func_name = "%s.%s" % (func.__module__, func.__name__)
        job._args = args
        job._kwargs = kwargs
        job.save()
        return job

    @classmethod
    def fetch(cls, pickle_data):
        func_name, args, kwargs = loads(str(pickle_data))
        job = cls()
        job._func_name = func_name
        job._args = args
        job._kwargs = kwargs
        job.save()
        return job


    def __init__(self):
        self._func_name = None
        self._args = None
        self._kwargs = None
        self._data = None

    def save(self):
        self._data = dumps((self._func_name, self._args, self._kwargs))

    def perform(self):
        module_name, func_name = self._func_name.rsplit('.', 1)
        module = importlib.import_module(module_name)
        func = getattr(module, func_name)
        return func(*self._args, **self._kwargs)






