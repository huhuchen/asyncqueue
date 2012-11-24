#!/usr/bin/env python
# -*- coding: utf-8 -*-

import asyncqueue

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

requires = [
    "redis",
    ]

setup(
    name="asyncqueue",
    version=asyncqueue.__version__,
    description="",
    author="huhuchen",
    author_email="",
    license="MIT",
    install_requires=requires,
    tests_require=requires,
    packages=find_packages(),
)
