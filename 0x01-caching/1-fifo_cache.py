#!/usr/bin/env python3
"""FIFO."""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Last In First Out."""

    def __init__(self):
        """Construct method."""
        super().__init__()

    def put(self, key, item):
        """."""
        if not key and not item:
            return
        self.cache_data[key] = item

        if len(self.cache_data) > self.MAX_ITEMS:
            cd = self.cache_data
            f_key = [*cd.keys()][0]
            cd.pop(f_key)
            print(f"DISCARD: {f_key}")

    def get(self, key):
        """Get data with key."""
        return self.cache_data.get(key)
