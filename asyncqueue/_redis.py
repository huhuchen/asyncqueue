#!/usr/bin/env python
# -*- coding: utf-8 -*-

import redis
import json

class Redis(object):

    def __init__(self, host="localhost", port=6379):
        self._host = host
        self._port = port
        self._redis_cursor = None

    def conn(self):
        if self._redis_cursor is None:
            pool = redis.ConnectionPool(host=self._host, port=self._port, db=0)
            self._redis_cursor = redis.Redis(connection_pool=pool)

    def enqueue(self, qname, data):
        self.conn()
        self._redis_cursor.rpush(qname, json.dumps(data))

    def dequeue(self, qname):
        self.conn()
        r = self._redis_cursor.blpop(qname)
        return json.loads(r[1])

if __name__ == "__main__":
    pass
