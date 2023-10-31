#!/usr/bin/env python3

"""Writing strings to Redis"""
import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """decorator methods"""

    @wraps(method)
    def wrapper(self, *args, **kwargs) -> bytes:
        """Counting the number of time a method is called"""
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


class Cache:
    """Class Chache"""

    def __init__(self) -> None:
        """Init"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
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
