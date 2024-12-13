#!/usr/bin/env python3

"""
Module that defines an asynchronous coroutine `async_generator`
which yields random numbers between 0 and 10.
"""

import asyncio
import random


async def async_generator():
    """
    Asynchronously generates a sequence of 10 random numbers.

    Each number is generated after an asynchronous delay of 1 second.

    Yields:
        float: A random float number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
