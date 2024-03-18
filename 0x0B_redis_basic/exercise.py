#!/usr/bin/env python3
''' Cache class to store and retrieve data from Redis '''

import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    ''' Count the number of times a method is called '''
    name = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.incr(name)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    ''' Cache class to store and retrieve data from Redis'''
    def __init__(self):
        self._redis = redis.Redis(host='localhost', port=6379, db=0)
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        ''' Store data in Redis and return a unique key'''
        unique_key = str(uuid.uuid4())
        self._redis.set(unique_key, data)
        return unique_key

    def get(self, key: str, fn: Callable =
            None) -> Union[str, bytes, int, float]:
        ''' Get data from Redis using a key and return as bytes
        or apply a function to the result before returning it.'''
        key = self._redis.get(key)
        if fn:
            return fn(key)

        return key

    def get_str(self, key: str) -> Optional[str]:
        ''' Get data from Redis using a key and return as string'''
        return self._redis.get(key).decode('utf-8')

    def get_int(self, key: str) -> Optional[int]:
        ''' Get data from Redis using a key and return as int'''
        value = self._redis.get(key)
        try:
            value = int(value.decode('utf-8'))
        except Exception:
            value = 0
            return value


if __name__ == "__main__":
    cache = Cache()
    key = cache.store("test data")
    print(key)
