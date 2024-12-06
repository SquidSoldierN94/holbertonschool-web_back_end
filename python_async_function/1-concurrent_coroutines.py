#!/usr/bin/env python3

"""
This script defines an asynchronous coroutine `wait_n` that spawns multiple
calls to the `wait_random` coroutine and returns the list of delays in
ascending order. It uses `asyncio` to manage concurrency.
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:

    """
    Spawns `wait_random` n times with the specified max_delay and returns
    the delays in ascending order.

    Args:
        n (int): The number of times to call `wait_random`.
        max_delay (int): The maximum delay for each `wait_random` call.

    Returns:
        List[float]: A list of delays sorted in ascending order.
    """
    delays = [wait_random(max_delay) for _ in range(n)]
    return [delay for delay in await asyncio.gather(*delays)]
