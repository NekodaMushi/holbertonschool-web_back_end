#!/usr/bin/env python3

"""Writing strings to Redis"""
import redis
import uuid


class Cache:
    """Class Chache"""

    def __init__(self) -> None:
        """Init"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: [str, bytes, int, float]) -> str:
        """Store data"""
        key = str(uuid.uuid1())
        self._redis.set(key, data)
        return key
