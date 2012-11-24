#!/usr/bin/env python
# -*- coding: utf-8 -*-

import redis
import json
from asyncqueue import REDIS_HOST, REDIS_PORT

pool = redis.ConnectionPool(host=REDIS_HOST, port=REDIS_PORT, db=0)
redis_cursor = redis.Redis(connection_pool=pool)


def enqueue(qname, data):
    redis_cursor.rpush("queue:%s"%qname, json.dumps(data))

def dequeue(qname):
    r = redis_cursor.blpop("queue:%s"%qname)
    return json.loads(r[1])
