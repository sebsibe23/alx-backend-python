#!/usr/bin/env python3
'''Task 2's module.
'''
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''Computes the average runtime of wait_n.

    Parameters:
        - n: The number of times to execute wait_n (integer)
        - max_delay: The maximum delay in seconds (integer)

    Returns:
        The average runtime of wait_n in seconds (float)
    '''
    try:
        start_time = time.time()
        asyncio.run(wait_n(n, max_delay))
        return (time.time() - start_time) / n
    except Exception as e:
        raise e
