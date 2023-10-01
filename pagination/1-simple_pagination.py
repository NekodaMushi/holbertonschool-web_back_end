#!/usr/bin/env python3
import csv
from typing import List

"""
Holberton task"""


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
        Makes two integer arguments page
        with default value 1 and page_size
          with default value 10.
        """
        assert (
            isinstance(page, int) and page > 0
        ), "Page should be an int and superior than 0"

        assert (
            isinstance(page_size, int) and page_size > 0
        ), "Page size should be an int and superior than 0"

        start_index, end_index = index_range(page, page_size)
        data_set = self.dataset()[start_index:end_index]

        return data_set
