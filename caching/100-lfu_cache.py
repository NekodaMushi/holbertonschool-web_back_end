#!/usr/bin/python3

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.frequency_keys = {}

    def put(self, key, item):
        if key is None or item is None:
            return

        immune_new_key = key
        if key in self.frequency_keys:
            self.frequency_keys[key] += 1
        else:
            self.frequency_keys[key] = 1
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            temp_safe_for_key = self.frequency_keys.pop(immune_new_key, None)
            discarded_key = min(
                self.frequency_keys, key=lambda x: self.frequency_keys[x]
            )

            print("-----")
            for x in self.frequency_keys:
                print(f"{x} -> {self.frequency_keys[x]}")
            print("-----")
            del self.cache_data[discarded_key]
            del self.frequency_keys[discarded_key]
            print(f"DISCARD: {discarded_key}")

            if temp_safe_for_key is not None:
                self.frequency_keys[immune_new_key] = temp_safe_for_key

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None
        self.frequency_keys[key] += 1
        return self.cache_data[key]
