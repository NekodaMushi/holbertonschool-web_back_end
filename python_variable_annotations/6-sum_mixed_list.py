#!/usr/bin/env python3
"""
    Basic annotations - sum_mixed_list
"""

from typing import List, Union


def sum_mixed_list(nxd_lst: List[Union[int, float]]) -> float:
    """
    Calculates the sum of a list of numbers
      (integers and/or floats) and returns it as a float.

    Args:
        nxd_lst (List[Union[int, float]]):
          The list of numbers (integers and/or floats) to be summed.

    Returns:
        float: The sum of the numbers in 'nxd_lst'.
    """
    return sum(nxd_lst)
