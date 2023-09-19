#!/usr/bin/env python3
"""
    Async annotations - task_wait_random
"""

from asyncio import Task
import asyncio

# Import the wait_random function
wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> Task:
    """
    Creates an asyncio Task that asynchronously waits for a random delay.

    Args:
        max_delay (int): The maximum delay time in seconds.

    Returns:
        Task: An asyncio Task that represents the asynchronous operation.
    """
    return asyncio.ensure_future(wait_random(max_delay))
