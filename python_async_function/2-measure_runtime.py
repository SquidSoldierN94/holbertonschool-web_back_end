#!/usr/bin/env python3
import asyncio
import time
from typing import Union
from 1-concurrent_coroutines import wait_n

def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay),
    and returns total_time / n.

    Parameters:
    n (int): Number of times to call wait_random.
    max_delay (int): Maximum delay value for wait_random.

    Returns:
    float: Average time per wait_random call.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
