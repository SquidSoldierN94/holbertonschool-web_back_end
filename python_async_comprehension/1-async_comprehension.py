#!/usr/bin/env python3

"""
Module that defines an asynchronous coroutine `async_comprehension`
which comprehends over `async_generator`.
"""

import asyncio
from typing import List

async_generator = __import__(
    '0-async_generator', fromlist=['async_generator']
).async_generator


async def async_comprehension() -> List[float]:
    """
    Collects values over `async_generator`.

    The coroutine collects and returns 10 random numbers as a list.

    Returns:
        List[float]: A list of 10 random float numbers between 0 and 10.
    """
    return [number async for number in async_generator()]
