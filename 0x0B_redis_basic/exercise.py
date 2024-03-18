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


def call_history(method: Callable) -> Callable:
    ''' Store the history of inputs and outputs for a particular function '''
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        input = str(args)
        self._redis.rpush(method.__qualname__ + ":inputs", input)

        output = str(method(self, *args, **kwargs))
        self._redis.rpush(method.__qualname__ + ":outputs", output)
        return output

    return wrapper


def replay(func: Callable):
    """ Replay function """
    r = redis.Redis()
    func_name = func.__qualname__
    number_calls = r.get(func_name)

    try:
        number_calls = number_calls.decode('utf-8')
    except Exception:
        number_calls = 0

    print(f'{func_name} was called {number_calls} times:')

    ins = r.lrange(func_name + ":inputs", 0, -1)
    outs = r.lrange(func_name + ":outputs", 0, -1)

    for cin, cout in zip(ins, outs):
        try:
            cin = cin.decode('utf-8')
        except Exception:
            cin = ""
        try:
            cout = cout.decode('utf-8')
        except Exception:
            cout = ""

        print(f'{func_name}(*{cin}) -> {cout}')


class Cache:
    ''' Cache class to store and retrieve data from Redis'''
    def __init__(self):
        self._redis = redis.Redis(host='localhost', port=6379, db=0)
        self._redis.flushdb()

    @count_calls
    @call_history
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
    cache.store("foo")
    cache.store("bar")
    cache.store(42)
    replay(cache.store)
