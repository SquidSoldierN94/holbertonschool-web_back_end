#!/usr/bin/env python3

import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between 0 and max_delay seconds.
    
    Args:
        max_delay (int): The maximum delay in seconds. Must be a non-negative integer. Defaults to 10.
        
    Returns:
        float: The actual delay time.
    
    Raises:
        TypeError: If max_delay is not an integer.
        ValueError: If max_delay is negative.
    """
    if not isinstance(max_delay, int):
        raise TypeError("max_delay must be an integer")
    
    if max_delay < 0:
        raise ValueError("max_delay must be non-negative")
    
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
