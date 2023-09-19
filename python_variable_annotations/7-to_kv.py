#!/usr/bin/env python3
"""
    Basic annotations - to_kv
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes a string 'k' and a number 'v' (int or float), and returns a tuple with 'k' and the square of 'v'.

    Args:
        k (str): The input string.
        v (Union[int, float]): The input number (int or float).

    Returns:
        Tuple[str, float]: A tuple containing 'k' and the square of 'v'.
    """
    return k, v**2
