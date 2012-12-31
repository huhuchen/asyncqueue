#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""tests for asyncqueue"""

from time import sleep
import unittest
from  asyncqueue import queue

async = queue(["greet",])

@async("greet")
def greet_friends(friend_name):
    greetings = "come on! %s" % friend_name
    return {"greetings": greetings}

@async("greet")
def greet_teacher(teacher_name):
    greetings = "hello! %s" % teacher_name
    return {"greetings": greetings}

def handler():
    friend_name = "Tom"

    greet_friends.delay(friend_name)

    teacher_name = "John"

    greet_teacher.delay(teacher_name)

    while True:
        print  async.worker("greet")

class AsyncqueueTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_handler(self):
        handler()


