#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination.
"""

import csv
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Loads the dataset from a CSV file if not already loaded.

        Returns:
            List[List]: The dataset as a list of lists.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE, encoding="utf-8") as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Remove header

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Indexes the dataset to allow deletion-resilient pagination.

        Returns:
            Dict[int, List]: A dictionary with indices as keys and values.
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }

        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Returns a dictionary for deletion-resilient pagination.

        Args:
            index (int): The start index of the return page.
            page_size (int): The number of items per page.

        Returns:
            Dict: A dictionary containing:
                - `index`: The current start index.
                - `next_index`: The next index to query.
                - `page_size`: The current page size.
                - `data`: The actual page of dataset.
        """
        assert isinstance(index, int) and 0 <= index < len(
            self.indexed_dataset()
        ), "Invalid index"

        data = []
        next_index = index
        dataset = self.indexed_dataset()

        while len(data) < page_size and next_index < len(self.dataset()):
            if next_index in dataset:
                data.append(dataset[next_index])
            next_index += 1

        return {
            "index": index,
            "next_index": next_index,
            "page_size": len(data),
            "data": data,
        }
