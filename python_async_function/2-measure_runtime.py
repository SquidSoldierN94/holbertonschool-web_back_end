#!/usr/bin/env python3

"""
This script defines a function `measure_time` that measures the total time
taken for `wait_n(n, max_delay)` to run and returns the average time per call.
It uses `time` to measure the elapsed time and `asyncio` to run the coroutines.
"""

import asyncio
import time
from typing import List

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:

    """
    Measures the total time taken for `wait_n(n, max_delay)` to run.

    Args:
        n (int): The number of times to call `wait_random`.
        max_delay (int): The maximum delay for each call to `wait_random`.

    Returns:
        float: The average time per call.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start_time
    return total_time / n
