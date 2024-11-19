from collections import deque
from typing import Any


class LRUCache:

    def __init__(self, capacity=16):
        self.capacity = capacity
        self._cache = dict()
        self._lru = deque()


    def put(self, key, value) -> None:
        if key in self._cache:
            self._lru.remove(key)
        else:
            if self._need_recache:
                lru_element = self._lru.popleft()
                self._cache.pop(lru_element)
        self._lru.append(key)
        self._cache[key] = value


    def get(self, key) -> Any:
        val = None
        if key in self._cache:
            self._lru.remove(key)
            self._lru.append(key)
            val = self._cache[key]

        return val

    @property
    def _need_recache(self) -> bool:
        return self.capacity == len(self._cache)