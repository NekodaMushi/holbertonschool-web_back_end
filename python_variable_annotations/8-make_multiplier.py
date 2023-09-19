#!/usr/bin/env python3
"""
    Basic annotations - make_multiplier
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Creates a multiplier function.

    Args:
        multiplier (float): The value by which
          the input number will be multiplied.

    Returns:
        Callable[[float], float]: A function that
          takes a float 'x' and returns 'x' multiplied by 'multiplier'.
    """

    def multiplier_function(x: float) -> float:
        """
        Multiplies a number by the specified multiplier.

        Args:
            x (float): The input number to be multiplied.

        Returns:
            float: The result of 'x' multiplied by the 'multiplier'.
        """
        return x * multiplier

    return multiplier_function
