#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""tests for asyncqueue"""

import unittest
import asyncqueue

async = asyncqueue.Queue(["mail", "vm"])

@async.send("vm")
def test1():
    return {"vm": "create"}

class AsyncqueueTestCase(unittest.TestCase):

    def setUp(self):


        pass

    def tearDown(self):
        pass

    def test_print_message(self):
        test1()
        m = asyncqueue.dequeue("vm")
        print "m", m
        self.assertNotEqual(m, None)


if __name__ == "__main__":
    unittest.main()
