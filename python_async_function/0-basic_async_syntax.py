#!/usr/bin/env python3
"""
    Async annotations - wait_random
"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronously waits for a random delay and
      returns the delay time.

    Args:
        max_delay (int): The maximum delay time
          in seconds (default is 10).

    Returns:
        float: The random delay time in seconds.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
