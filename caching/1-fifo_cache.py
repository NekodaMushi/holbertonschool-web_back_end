#!/usr/bin/python3
"""
FIFO caching - FIFOCache class
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    A caching class that implements a First-In-First-Out
      (FIFO) eviction policy.

    Methods:
        __init__(self): Initialize the FIFOCache.
        put(self, key, item): Store an item in the cache.
        get(self, key): Retrieve an item from the cache.

    Attributes:
        cache_data (dict): A dictionary to store cached data.
        keys (list): A list to maintain the order
          of keys based on the FIFO policy.
    """

    def __init__(self):
        """
        Initialize the FIFOCache.
        """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """
        Store an item in the cache.

        Args:
            key: The key for the item.
            item: The item to be stored.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
        if key not in self.keys:
            self.keys.append(key)

        if len(self.keys) > BaseCaching.MAX_ITEMS:
            discarded_key = self.keys.pop(0)
            del self.cache_data[discarded_key]
            print(f"DISCARD: {discarded_key}")

    def get(self, key):
        """
        Retrieve an item from the cache.

        Args:
            key: The key for the item to retrieve.

        Returns:
            The cached item if found, otherwise None.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
