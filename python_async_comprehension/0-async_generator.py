#!/usr/bin/env python3
"""
    Async annotations - async_generator
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronous generator that yields
      random floats between 0 and 10.

    Yields:
        float: A random float between 0 and 10.
    """
    for x in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
