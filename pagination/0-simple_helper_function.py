#!/usr/bin/env python3
"""
Module to get the start index and end index for pagination
"""


from typing import Tuple


def index_range(page, page_size) -> Tuple[int, int]:
    """
    get up
    """

    start = (page - 1) * page_size
    end = start + page_size

    return (start, end)