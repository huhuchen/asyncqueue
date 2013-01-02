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
        if inspect.ismethod(func):
            job._instance = func.im_self
            job._func_name = func.__name__
        elif inspect.isfunction(func):
            job._func_name = "%s.%s" % (func.__module__, func.__name__)
        job._args = args
        job._kwargs = kwargs
        job.save()
        return job

    @classmethod
    def fetch(cls, data):
        func_name, instance, args, kwargs = loads(str(data))
        job = cls()
        job._func_name = func_name
        job._args = args
        job._kwargs = kwargs
        job._instance = instance
        job.save()
        return job


    def __init__(self):
        self._func_name = None
        self._instance = None
        self._args = None
        self._kwargs = None
        self._data = None

    def save(self):
        self._data = dumps((self._func_name, self._instance, self._args, self._kwargs))

    def perform(self):
        if self._instance:
            return getattr(self._instance, self._func_name)

        module_name, func_name = self._func_name.rsplit('.', 1)
        module = importlib.import_module(module_name)
        func = getattr(module, func_name)
        return func(*self._args, **self._kwargs)
