#!/usr/bin/python3
"""
FIFOCache module
"""

BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """BasicCache class"""

    def __init__(self):
        """Constructor"""
        super().__init__()
        self._next_discarded_key_index = 0

    def put(self, key, item):
        """Add an item in the cache"""
        if key is not None and item is not None:
            if len(self.cache_data) != 4 or key in self.cache_data.keys():
                self.cache_data[key] = item
            else:
                if self._next_discarded_key_index + 1 < self.MAX_ITEMS:
                    self._next_discarded_key_index = 0

                discarded_key = sorted(self.cache_data.keys())[
                    self._next_discarded_key_index
                ]
                del self.cache_data[discarded_key]
                print(f"DISCARD: {discarded_key}")
                self.cache_data[key] = item
                self._next_discarded_key_index += 1

    def get(self, key):
        """Get an item by key"""
        return self.cache_data.get(key, None)
