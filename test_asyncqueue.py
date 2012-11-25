#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""tests for asyncqueue"""

import unittest
import asyncqueue

async = asyncqueue.queue(["mail", "vm"])

@async.enqueue("greet")
def test1():
    return {"greetings": "hello"}

class AsyncqueueTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_print_message(self):
        test1()
        m = async.dequeue("vm")
        print "m", m
        self.assertNotEqual(m, None)


if __name__ == "__main__":
    unittest.main()
