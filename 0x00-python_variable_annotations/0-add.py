#!/usr/bin/env python3
'''
This module contains a function called 'add' that adds two
floating-point numbers.

Usage Example:
result = add(3.5, 4.2)
print(result)  # Output: 7.7
'''


def add(a: float, b: float) -> float:
    '''Adds two floating-point numbers.'''
    try:
        return a + b
    except TypeError:
        raise TypeError("Both 'a' and 'b' must be floating-point numbers.")
