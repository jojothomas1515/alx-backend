#!/usr/bin/env python3
"""Basic Cache Module."""

from base_caching import BaseCaching

class BasicCache(BaseCaching):
    """Create a basic cache instance."""


    def put(self, key, item) -> None:
        """Add item to the cache_data.

        Args:
        key: the key of that value to be stored.
        item: to be added to the cache.
        """
        if not key or not item:
            return

        self.cache_data[key] = item

    def get(self, key):
        """Get item from the cache data.

        Args:
        key: use to get item from the cache data data.
        """
        return self.cache_data.get(key)
