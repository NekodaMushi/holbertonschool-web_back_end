#!/usr/bin/env python3
"""
    Async comprehension - async_comprehension
"""

from typing import List

# Import the async_generator function
async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """
    Asynchronously generates and returns a list of floats using async comprehension.

    Returns:
        List[float]: A list of floats generated asynchronously.
    """
    return [number async for number in async_generator()]
