#!/usr/bin/env python3
'''Task 3's module.
'''
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''Creates an asynchronous task for wait_random.

    Parameters:
        - max_delay: The maximum delay in seconds (integer)

    Returns:
        An asyncio.Task representing the execution of wait_random
    '''
    try:
        return asyncio.create_task(wait_random(max_delay))
    except Exception as e:
        raise e
