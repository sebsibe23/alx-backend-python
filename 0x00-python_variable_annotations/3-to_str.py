#!/usr/bin/env python3
'''
This module contains a function
called 'to_str' that converts
a floating-point number to a string.

Usage Example:
result = to_str(3.14)
print(result)  # Output: "3.14"
'''


def to_str(n: float) -> str:
    '''Converts a floating-point number
    to a string.'''
    try:
        return str(n)
    except TypeError:
        raise TypeError("The input 'n' must be a floating-point number.")
