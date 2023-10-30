#!/usr/bin/env python3

"""Writing strings to Redis"""
import redis
import uuid
from typing import Union, Callable, Optional


class Cache:
    """Class Chache"""

    def __init__(self) -> None:
        """Init"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data"""
        key = str(uuid.uuid1())
        self._redis.set(key, data)
        return key

    def get(
        self, key: str, fn: Optional[Callable] = None
    ) -> Union[str, bytes, int, float]:
        """Convert and get data"""
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_str(self, data: str) -> str:
        """automatically parametrize Cache.get with the correct conversion function"""
        return data.decode("utf-8")

    def get_int(self, data: str) -> int:
        """automatically parametrize Cache.get with the correct conversion function"""
        return int(data)
