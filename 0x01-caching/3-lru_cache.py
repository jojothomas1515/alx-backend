#!/usr/bin/env python3
"""LRU cache module."""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """Last Recently Used cache class to create instance."""

    def put(self, key, item):
        """Put method for cache insertion.

        Args:
        key: identifier for item in the cache dick
        item: item to add to the cache
        """
        if not key or not item:
            return
        if self.cache_data.get(key):
            self.cache_data.pop(key)
        self.cache_data[key] = item

        if len(self.cache_data) > self.MAX_ITEMS:
            di = self.cache_data
            k = [*di.keys()][0]
            di.pop(k)
            print(f"DISCARD: {k}")

    def get(self, key):
        """Get data with key.

        Args:
        key: identifier for item to get from cache
        Return: item or None
        """

        item = self.cache_data.get(key)
        if item:
            self.put(key, item)
        return item
