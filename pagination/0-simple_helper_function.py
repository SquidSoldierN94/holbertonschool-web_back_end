#!/usr/bin/env python3
"""
Module to get the start index and end index for pagination
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns a tuple containing the start index and end index
    corresponding to the range of indexes to return in a list
    for a given pagination.

    Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing (start index, end index).
    """

    if not isinstance(page, int) or not isinstance(page_size, int):
        raise TypeError("Both page and page_size must be integers")

    if page <= 0 or page_size <= 0:
        raise ValueError("Both page and page_size must be positive integers")

    start = (page - 1) * page_size
    end = start + page_size

    return (start, end)
