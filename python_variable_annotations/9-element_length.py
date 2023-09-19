#!/usr/bin/env python3
"""
    Basic annotations - element_length
"""

from typing import Iterable, Tuple, Sequence, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculates the length of elements in an iterable of sequences and returns a list of tuples.

    Args:
        lst (Iterable[Sequence]): An iterable of sequences (e.g., lists, strings).

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where each tuple contains a sequence from 'lst'
        and its corresponding length.
    """
    return [(i, len(i)) for i in lst]
