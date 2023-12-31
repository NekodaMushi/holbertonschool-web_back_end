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


def call_history(method: Callable) -> Callable:
    """decorator methods"""
    inputs = f"{method.__qualname__}:inputs"
    outputs = f"{method.__qualname__}:outputs"

    @wraps(method)
    def wrapper(self, *args, **kwargs) -> bytes:
        """Store history of inputs & outputs"""
        self._redis.rpush(inputs, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(outputs, output)
        return output

    return wrapper


def replay(method: Callable) -> Callable:
    """display history of calls"""
    r = redis.Redis()
    count_keys = method.__qualname__
    count = int(r.get(count_keys))

    print(f"{method.__qualname__} was called {count} times:")

    inputs = f"{method.__qualname__}:inputs"
    outputs = f"{method.__qualname__}:outputs"

    r_inputs = r.lrange(inputs, 0, -1)
    r_outputs = r.lrange(outputs, 0, -1)

    for inp, out in zip(r_inputs, r_outputs):
        inp_str = inp.decode("utf-8")
        out_str = out.decode("utf-8")
        print(f"{method.__qualname__}(*{inp_str}) -> {out_str}")


class Cache:
    """Class Chache"""

    def __init__(self) -> None:
        """Init"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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
        """automatically parametrize Cache.get
        with the correct conversion function"""
        return data.decode("utf-8")

    def get_int(self, data: str) -> int:
        """automatically parametrize Cache.get
        with the correct conversion function"""
        return int(data)
