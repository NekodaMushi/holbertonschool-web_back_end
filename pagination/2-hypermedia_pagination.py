#!/usr/bin/env python3
"""
    Simple helper function
"""

import csv
from typing import List
import math


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
    index_start = (page - 1) * page_size
    index_end = index_start + page_size

    return index_start, index_end


class Server:
    """
    Server class to paginate a database of popular baby names.
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get the asked page
        """
        assert (
            isinstance(page, int) and page > 0
        ), "Page should be an int and superior to 0"

        assert (
            isinstance(page_size, int) and page_size > 0
        ), "Page size should be an int and superior to 0"

        start_index, end_index = index_range(page, page_size)
        data_set = self.dataset()[start_index:end_index]

        return data_set

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Retrieve the key value pair of the dictionary
        """
        data = self.get_page(page, page_size)

        total_row = len(self.dataset())
        total_pages = math.ceil(total_row / page_size)

        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        data_dict = {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages,
        }

        return data_dict
