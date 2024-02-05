#!/usr/bin/python3
''' BasicCache class '''
from base_caching import BaseCaching



class BasicCache(BaseCaching):
    """ Defines a class BasicCache that inherits from BaseCaching
      and is a caching system """

    def put(self, key, item):
        ''' Add an item to the cache'''
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        ''' Get an item by key '''
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
