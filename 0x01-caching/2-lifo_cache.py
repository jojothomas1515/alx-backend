#!/usr/bin/env python3
"""LIFO."""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Last In First Out."""

    def put(self, key, item):
        """."""
        if not key and not item:
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
        """Get data with key."""
        return self.cache_data.get(key)
