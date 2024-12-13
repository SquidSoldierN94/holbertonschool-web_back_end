#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict, Any

class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict[str, Any]:
        """
        Return a dictionary with pagination information that is resilient to deletions.

        Args:
            index (int): The start index for the current page (0-indexed).
            page_size (int): The number of items per page.

        Returns:
            Dict[str, Any]: A dictionary containing pagination information.
        """
        assert isinstance(index, int) and index >= 0, "index must be a non-negative integer"
        assert isinstance(page_size, int) and page_size > 0, "page_size must be an integer greater than 0"

        indexed_dataset = self.indexed_dataset()
        dataset_len = len(indexed_dataset)
        assert index < dataset_len, "index is out of range"

        data = []
        next_index = index
        current_count = 0

        while current_count < page_size and next_index < dataset_len:
            if next_index in indexed_dataset:
                data.append(indexed_dataset[next_index])
                current_count += 1
            next_index += 1

        next_index = next_index if next_index < dataset_len else None

        return {
            'index': index,
            'data': data,
            'page_size': len(data),
            'next_index': next_index
        }
