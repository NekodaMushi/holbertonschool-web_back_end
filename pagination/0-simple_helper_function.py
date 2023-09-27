#!/usr/bin/env python3
"""
    Pagination - index_range
"""


def index_range(page, page_size):
    """
    Get the start and end indices for a given page and page size.

    Args:
        page (int): The page number.
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple containing the start and end indices (inclusive)
        for the specified page.
    """

    if page <= 0 or page_size <= 0:
        return None

    index_start = (page - 1) * page_size
    index_end = index_start + page_size - 1

    return index_start, index_end
