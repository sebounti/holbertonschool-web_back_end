#!/usr/bin/python3
''' LRU Caching System '''
from base_caching import BaseCaching


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
                lru_key = self.keys.pop(0)  # Évince l'élément LRU
                del self.cache_data[lru_key]
                print("DISCARD:", lru_key)
            self.cache_data[key] = item
            self.keys.append(key)

    def get(self, key):
        ''' Get an item by key
        '''
        if key is None or key not in self.cache_data:
            return None
        if key in self.keys:
            self.keys.remove(key)
            self.keys.append(key)
        return self.cache_data[key]
