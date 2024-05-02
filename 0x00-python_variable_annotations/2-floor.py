#!/usr/bin/env python3
'''
This module contains a function
called 'floor' that computes
the floor of a floating-point number.

Usage Example:
result = floor(3.7)
print(result)  # Output: 3
'''


def floor(a: float) -> int:
    '''Computes the floor of a floating-point number.'''
    try:
        return int(a)
    except TypeError:
        raise TypeError("The input 'a' must be a floating-point number.")
