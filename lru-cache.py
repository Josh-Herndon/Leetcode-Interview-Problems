from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.lru_cache = OrderedDict()

    def get(self, key):

        if key in self.lru_cache:
            val = self.lru_cache[key]
            del self.lru_cache[key]
            self.lru_cache[key] = val
            return val
        else:
            return -1

    def put(self, key, value):

        if key in self.lru_cache:
            del self.lru_cache[key]
            self.lru_cache[key] = value
            return

        if len(self.lru_cache) + 1 <= self.capacity:
            self.lru_cache[key] = value
        else:
            for _key in self.lru_cache:
                del self.lru_cache[_key]
                break

            self.lru_cache[key] = value