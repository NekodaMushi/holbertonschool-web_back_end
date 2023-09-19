#!/usr/bin/env python3

from typing import List
import asyncio

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = []

    for task in tasks:
        delay = await task
        delays.append(delay)

    return sorted(delays)
