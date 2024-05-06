#!/usr/bin/env python3
'''Task 0's module.
'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''Waits for a random number of seconds.

    Parameters:
        - max_delay: The maximum delay in seconds (integer, default: 10)

    Returns:
        The actual wait time in seconds (float)
    '''
    try:
        wait_time = random.random() * max_delay
        await asyncio.sleep(wait_time)
        return wait_time
    except Exception as e:
        raise e
