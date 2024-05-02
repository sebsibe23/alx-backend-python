#!/usr/bin/env python3
'''
This module contains a function
called 'make_multiplier' that creates
a multiplier function.

Usage Example:
multiply_by_2 = make_multiplier(2.0)
result = multiply_by_2(5.0)
print(result)  # Output: 10.0
'''

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Creates a multiplier function.'''
    try:
        return lambda x: x * multiplier
    except TypeError:
        raise TypeError("The input 'multiplier' must be a float.")
