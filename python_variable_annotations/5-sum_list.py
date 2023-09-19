#!/usr/bin/env python3
"""
    Basic annotations - sum_list
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculates the sum of a list of floating-point numbers and returns it as a float.

    Args:
        input_list (List[float]): The list of floating-point numbers to be summed.

    Returns:
        float: The sum of the numbers in 'input_list'.
    """
    return sum(input_list)
