#!/usr/bin/env python3
"""
Module to paginate simple data with hypermedia pagination.
"""

import csv
import math
from typing import List, Dict, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns a tuple containing the start and end indexes for pagination.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: (start index, end index)
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)


class Server:
    """
    Server class to handle dataset pagination with hypermedia response.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Loads the dataset from the CSV file if not already loaded.

        Returns:
            List[List]: The dataset as a list of lists.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE, encoding="utf-8") as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Remove header row

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Returns a page of data from the dataset.

        Args:
            page (int): The page number (1-indexed).
            page_size (int): The number of items per page.

        Returns:
            List[List]: The data corresponding to the requested page.
        """
        assert isinstance(page, int), "Page must be an integer"
        assert isinstance(page_size, int), "Page size must be an integer"
        assert page > 0, "Page must be a positive integer"
        assert page_size > 0, "Page size must be a positive integer"

        data = self.dataset()
        start, end = index_range(page, page_size)

        if start >= len(data):  # If the start index is out of range
            return []

        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Returns a dictionary containing pagination details.

        Args:
            page (int): The page number.
            page_size (int): The number of items per page.

        Returns:
            Dict: A dictionary containing pagination details.
        """
        data = self.get_page(page, page_size)
        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size)

        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages,
        }
