#!/usr/bin/python3
from base_caching import BaseCaching
''' LRU Caching System '''

class LRUCache(BaseCaching):
    ''' LRU Caching System '''
    def __init__(self):
        ''' Initiliaze
        '''
        super().__init__()
        self.keys = []

    def put(self, key, item):
        ''' Add an item in the cache
        '''
        if key is not None and item is not None:
                if key in self.cache_data:
                    self.keys.remove(key)
                elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    del self.cache_data[self.keys[0]]
                    print("DISCARD:", self.keys[0])
                    self.keys.pop(0)
                self.keys.append(key)
                self.cache_data[key] = item

    def get(self, key):
        ''' Get an item by key
        '''
        if key is None or key not in self.cache_data:
            return None
        self.keys.remove(key)
        self.keys.append(key)
        return self.cache_data[key]
