#!/usr/bin/env python3
import asyncio
from 0-basic_async_syntax import wait_random

def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create and return an asyncio.Task that runs wait_random with the specified max_delay.

    Parameters:
    max_delay (int): The maximum delay value for wait_random.

    Returns:
    asyncio.Task: A task that runs the wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
