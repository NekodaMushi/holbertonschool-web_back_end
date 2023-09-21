#!/usr/bin/python3

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.keys = []

    def put(self, key, item):
        if key is not None and item is not None:
            self.cache_data[key] = item
        if key not in self.keys:
            self.keys.append(key)

        if len(self.keys) > BaseCaching.MAX_ITEMS:
            discarded_key = self.keys.pop(0)
            print(f"DISCARD: {discarded_key}")

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
