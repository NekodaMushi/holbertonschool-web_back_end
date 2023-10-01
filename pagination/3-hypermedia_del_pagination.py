#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class for deletion-resilient hypermedia pagination."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {i: dataset[i] 
        for i in range(len(dataset))}
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        if between two queries, certain rows are removed from the dataset,
        the user does not miss items from dataset when changing page.
        """
        assert index is None or (
            isinstance(index, int) and index >= 0
        ), "Index should be a non-negative integer"
        assert (
            isinstance(page_size, int) and page_size > 0
        ), "Page size should be a positive integer"

        total_rows = len(self.dataset())

        next_index = index + page_size

        # Making sure start index is within a valid range
        if index is None:
            start_index = 0
        else:
            start_index = max(0, min(index, total_rows - 1))

        # Making sure next index is within a valid range
        next_index = max(0, min(next_index, total_rows))

        # Retrieve data for the current page, checking if the index exists
        data = [
            self.indexed_dataset().get(i)  # Use .get() to avoid KeyError
            for i in range(start_index, min(start_index + 
            page_size, total_rows))
        ]

        hyper_dict = {
            "index": start_index,
            "data": data,
            "next_index": next_index,
            "page_size": page_size,
        }

        return hyper_dict
