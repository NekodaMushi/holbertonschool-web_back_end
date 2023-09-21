#!/usr/bin/python3

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.keys = []

    def put(self, key, item):
        if key is None or item is None:
            return
        if key in self.keys:
            self.keys.remove(key)
        self.keys.append(key)
        self.cache_data[key] = item

        if len(self.keys) > BaseCaching.MAX_ITEMS:
            discarded_key = self.keys.pop(-2)
            del self.cache_data[discarded_key]
            print(f"DISCARD: {discarded_key}")

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
