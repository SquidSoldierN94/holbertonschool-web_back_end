#!/usr/bin/env python3

"""
This script defines a function `task_wait_random` that creates a task to run
the `wait_random` coroutine. It uses `asyncio.create_task` to schedule the
`wait_random` function as a task.
"""

import asyncio
from typing import Callable

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:

    """
    Creates a task to run the `wait_random` coroutine.

    Args:
        max_delay (int): The maximum delay for the `wait_random` call.

    Returns:
        asyncio.Task: A task for the `wait_random` coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
