#!/usr/bin/env python3
"""
Module to paginate simple data
"""

import csv
import math
from typing import List

index_range = __import__('0-simple_helper_function').index_range


class Server:
    """
    database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Function to get a specific page of the dataset
        """

        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0

        if (
                page > 10 or page_size > 10) or (
                    page < 1 or page_size < 1):
            return []

        data = self.dataset()

        start, end = index_range(page, page_size)
        return data[start:end]
