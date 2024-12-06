#!/usr/bin/env python3

"""
This script defines an asynchronous function `task_wait_n` that spawns
multiple `task_wait_random` tasks and gathers their results.
"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:

    """
    Calls `task_wait_random` n times and returns the list of delays.

    Args:
        n (int): The number of tasks to run.
        max_delay (int): The maximum delay for each call to `wait_random`.

    Returns:
        List[float]: A list of delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return [task.result() for task in await asyncio.gather(*tasks)]
