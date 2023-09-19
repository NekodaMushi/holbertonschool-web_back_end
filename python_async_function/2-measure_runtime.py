#!/usr/bin/env python3
"""
    Async annotations - measure_time
"""

import time
import asyncio

wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the average time taken to run 'n' concurrent asynchronous tasks.

    Args:
        n (int): The number of concurrent tasks.
        max_delay (int): The maximum delay time in seconds for each task.

    Returns:
        float: The average time taken for each task to complete.
    """
    t0 = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    t1 = time.perf_counter()

    total_time = t1 - t0

    return total_time / n
