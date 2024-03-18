#!/usr/bin/env python3
''' Cache class to store and retrieve data from Redis '''

import redis
import uuid
from typing import Union


class Cache:
    ''' Cache class to store and retrieve data from Redis'''
    def __init__(self):
        self._redis = redis.Redis(host='localhost', port=6379, db=0)
        self._redis.flushdb()


    def store(self, data: Union[str, bytes, int, float]) -> str:
        ''' Store data in Redis and return a unique key'''
        unique_key = str(uuid.uuid4())
        self._redis.set(unique_key, data)
        return unique_key


if __name__ == "__main__":
    cache = Cache()
    key = cache.store("test data")
    print(key)
