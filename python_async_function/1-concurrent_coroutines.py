#!/usr/bin/env python3
"""
    Async annotations - wait_n
"""

from typing import List


wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronously waits for 'n' random delays
      and returns a sorted list of delay times.

    Args:
        n (int): The number of delays to wait for.
        max_delay (int): The maximum delay time in seconds.

    Returns:
        List[float]: A sorted list of 'n' random delay times in seconds.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = []

    for task in tasks:
        delay = await task
        delays.append(delay)

    return sorted(delays)
