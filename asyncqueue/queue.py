#!/usr/bin/env python
# -*- coding: utf-8 -*-

import redis
import json

class Redis(object):

    def __init__(self, host="localhost", port=6379):
        self._host = host
        self._port = port
        self.redis_cursor = None

    def conn(self):
        pool = redis.ConnectionPool(host=self._host, port=self._port, db=0)
        self.redis_cursor = redis.Redis(connection_pool=pool)

    def enqueue(self, qname, data):
        self.conn()
        self.redis_cursor.rpush("queue:%s"%qname, json.dumps(data))

    def dequeue(self, qname):
        self.conn()
        r = self.redis_cursor.blpop("queue:%s"%qname)
        return json.loads(r[1])
