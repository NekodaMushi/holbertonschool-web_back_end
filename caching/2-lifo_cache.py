#!/usr/bin/python3
"""
LIFO caching - LIFOCache class
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    A caching class that implements a Last-In-First-Out (LIFO) eviction policy.

    Methods:
        __init__(self): Initialize the LIFOCache.
        put(self, key, item): Store an item in the cache.
        get(self, key): Retrieve an item from the cache.

    Attributes:
        cache_data (dict): A dictionary to store cached data.
        keys (list): A list to maintain the order of keys based on the LIFO policy.
    """

    def __init__(self):
        """
        Initialize the LIFOCache.
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
        if key is None or item is None:
            return
        if key in self.keys:
            self.keys.remove(key)
        self.keys.append(key)
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discarded_key = self.keys.pop(-2)
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
