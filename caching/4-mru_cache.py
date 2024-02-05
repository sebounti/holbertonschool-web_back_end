#!/usr/bin/python3
''' MRUCache class '''
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    ''' MRUCache class inherits from BaseCaching '''
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
                mru_keys = self.keys.pop()
                del self.cache_data[mru_keys]
                print(f"DISCARD:", mru_keys)
            self.cache_data[key] = item
            self.keys.append(key)

    def get(self, key):
        ''' Get an item by key
        '''
        if key is None or key not in self.cache_data:
            return None
        self.keys.remove(key)
        self.keys.append(key)
        return self.cache_data[key]
