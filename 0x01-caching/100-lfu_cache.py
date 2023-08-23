#!/usr/bin/env python3
"""LFU cache module."""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """Last Recently Used cache class to create instance."""

    def __init__(self):
        """Initialize lfu cache instance."""
        super().__init__()
        self.key_freq = {}

    def put(self, key, item):
        """Put method for cache insertion.

        Args:
        key: identifier for item in the cache dick
        item: item to add to the cache
        """
        if not key or not item:
            return

        if not self.cache_data.get(key) \
                and len(self.cache_data) + 1 > self.MAX_ITEMS:
            di = self.cache_data
            k = min(di, key=lambda x: self.key_freq.get(x))
            print(self.key_freq)

            di.pop(k)
            self.key_freq.pop(k)
            print(f"DISCARD: {k}")

        if self.cache_data.get(key):
            self.cache_data.pop(key)
        self.cache_data[key] = item
        if self.key_freq.get(key) is None:
            self.key_freq[key] = 0
        else:
            self.key_freq[key] = self.key_freq.get(key) + 1

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
