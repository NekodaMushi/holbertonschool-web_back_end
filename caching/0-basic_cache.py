#!/usr/bin/python3
"""
Basic caching - BasicCache class
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    A basic caching class that extends BaseCaching.

    Methods:
        put(self, key, item): Store an item in the cache.
        get(self, key): Retrieve an item from the cache.

    Attributes:
        cache_data (dict): A dictionary to store cached data.
    """

    def put(self, key, item):
        """
        Store an item in the cache.

        Args:
            key: The key for the item.
            item: The item to be stored.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache.

        Args:
            key: The key for the item to retrieve.

        Returns:
            The cached item if found, otherwise None.
        """
        if key in self.cache_data:
            return self.cache_data[key]
