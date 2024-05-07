#!/usr/bin/env python3
'''Task 1's module.
'''
try:
    from typing import List
    from importlib import import_module as using

    async_generator = using('0-async_generator').async_generator

    async def async_comprehension() -> List[float]:
        '''Creates a list of 10 numbers from a 10-number generator.

        Returns:
            A list of 10 floating-point numbers.
        '''
        return [num async for num in async_generator()]
except Exception as e:
    # If an exception occurs during the execution of the code,
    # this block catches the exception and handles it.
    handle_exception(e)
