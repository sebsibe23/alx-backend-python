#!/usr/bin/env python3
'''
This module contains a function
called 'to_kv' that converts a key
and its value to a tuple of the
key and the square of its value.

Usage Example:
key = "length"
value = 5
result = to_kv(key, value)
print(result)  # Output: ('length', 25.0)
'''

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''Converts a key and its value to
    a tuple of the key and the
    square of its value.
    '''
    try:
        return (k, float(v ** 2))
    except TypeError:
        raise TypeError("The input 'v' must be an integer or a float.")
