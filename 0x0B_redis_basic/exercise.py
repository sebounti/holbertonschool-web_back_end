#!/usr/bin/env python3
''' Cache class to store and retrieve data from Redis '''

import redis
import uuid
from typing import Union, Callable, Optional


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


    def get(self, key: str, fn: Optional[Callable[[bytes],
            Union[str, bytes, int, float]]] = None) -> Union[str,
                                                             bytes, int, float,
                                                               None]:
        ''' Get data from Redis using a key and return as bytes
        or apply a function to the result before returning it.'''
        result = self._redis.get(key)
        if result is not None and fn is not None:
            return fn(result)
        return result


    def get_str(self, key: str) -> Optional[str]:
        ''' Get data from Redis using a key and return as string'''
        return self.get(key, lambda x: x.decode('utf-8'))


    def get_int(self, key: str) -> Optional[int]:
        ''' Get data from Redis using a key and return as int'''
        result = self.get(key)
        try:
            return int(result) if result is not None else None
        except ValueError:
            return None



if __name__ == "__main__":
    cache = Cache()
    key = cache.store("test data")
    print(key)
