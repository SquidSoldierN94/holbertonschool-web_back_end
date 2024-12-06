#!/usr/bin/env python3
import asyncio
from typing import List
from 0-basic_async_syntax import wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronously spawns wait_random n times with the specified max_delay.

    Parameters:
    n (int): Number of times to spawn wait_random.
    max_delay (int): Maximum delay value for wait_random.

    Returns:
    List[float]: List of all delays in ascending order.
    """
    delays = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    return sorted(delays)
