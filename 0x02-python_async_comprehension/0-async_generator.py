#!/usr/bin/env python3
'''Task 0's module.
'''
try:
    import asyncio
    import random
    from typing import Generator

    async def async_generator() -> Generator[float, None, None]:
        '''Generates a sequence of 10 numbers.

        Yields:
            Floating-point numbers from a generator.
        '''
        for _ in range(10):
            await asyncio.sleep(1)
            yield random.random() * 10
except Exception as e:
    handle_exception(e)
