#!/usr/bin/python3
""" FIFOCache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ caching system
    """
    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.__queue = []

    def put(self, key, item):
        """ Adds an item in the cache
        """
        if not key or not item:
            return
        if key not in self.__queue:
            self.__queue.append(key)
        if len(self.__queue) > self.MAX_ITEMS:
            self.cache_data.pop(self.__queue[0])
            print('DISCARD: {}'.format(self.__queue.pop(0)))
        self.cache_data.update({key: item})

    def get(self, key):
        """ Gets an item by key
        """
        return self.cache_data.get(key)
