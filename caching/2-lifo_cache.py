#!/usr/bin/python3
from base_caching import BaseCaching
''' LIFOCache class '''

class LIFOCache(BaseCaching):
    ''' LIFOCache class inherits from BaseCaching '''
    def __init__(self):
        ''' Initiliaze
        '''
        super().__init__()
        self.keys = []

    def put(self, key, item):
        ''' Add an item in the cache
        '''
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if key not in self.cache_data:
                    del self.cache_data[self.keys[-1]]
                    print("DISCARD:", self.keys[-1])
                    self.keys.pop(-1)
            self.cache_data[key] = item
            self.keys.append(key)

    def get(self, key):
        ''' Get an item by key
        '''
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
