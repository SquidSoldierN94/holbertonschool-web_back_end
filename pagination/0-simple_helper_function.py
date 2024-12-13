#!/usr/bin/env python3

"""
Module that defines a function `index_range` which returns the start
and end index for pagination.
"""

def index_range(page: int, page_size: int) -> tuple:
    """
    Calculate the start and end indexes for a given page and page size.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple containing the start index and the end index.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
