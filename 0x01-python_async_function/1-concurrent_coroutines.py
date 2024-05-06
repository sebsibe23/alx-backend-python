#!/usr/bin/env python3
'''Task 1's module.
'''
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''Executes wait_random n times.

    Parameters:
        - n: The number of times to execute wait_random (integer)
        - max_delay: The maximum delay in seconds (integer)

    Returns:
        A list of the actual wait times in seconds (List[float])
    '''
    try:
        wait_times = await asyncio.gather(
            *tuple(map(lambda _: wait_random(max_delay), range(n)))
        )
        return sorted(wait_times)
    except Exception as e:
        raise e
