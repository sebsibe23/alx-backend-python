#!/usr/bin/env python3
'''Task 4's module.
'''
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''Executes task_wait_random n times.

    Parameters:
        - n: The number of times to execute task_wait_random (integer)
        - max_delay: The maximum delay in seconds (integer)

    Returns:
        A list of the actual wait times in seconds (List[float])
    '''
    try:
        wait_times = await asyncio.gather(
            *tuple(map(lambda _: task_wait_random(max_delay), range(n)))
        )
        return sorted(wait_times)
    except Exception as e:
        raise e
