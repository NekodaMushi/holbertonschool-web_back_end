#!/usr/bin/env python3
"""
    Async comprehension - measure_runtime
"""

import time
import asyncio

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """
    Measures the total runtime for running
      async_comprehension() four times concurrently.

    Returns:
        float: The total runtime in seconds.
    """
    t0 = time.time()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    t1 = time.time()

    measure = t1 - t0

    return measure
