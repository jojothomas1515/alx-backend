#!/usr/bin/env python3
"""FIFO cache module."""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Last In First class to create cache instance."""

    def put(self, key, item):
        """Put method for cache insertion.

        Args:
        key: identifier for item in the cache dick
        item: item to add to the cache
        """
        if not key and not item:
            return
        self.cache_data[key] = item

        if len(self.cache_data) > self.MAX_ITEMS:
            cd = self.cache_data
            f_key = [*cd.keys()][0]
            cd.pop(f_key)
            print(f"DISCARD: {f_key}")

    def get(self, key):
        """Get data with key.

        Args:
        key: identifier for item to get from cache
        Return: item or None
        """
        return self.cache_data.get(key)
