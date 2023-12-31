#!/usr/bin/env python3
"""LIFO cache module."""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Last In First Out."""

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
            k = [*di.keys()][-2]
            di.pop(k)
            print(f"DISCARD: {k}")

    def get(self, key):
        """Get data with key.

        Args:
        key: identifier for item to get from cache
        Return: item or None
        """
        return self.cache_data.get(key)
