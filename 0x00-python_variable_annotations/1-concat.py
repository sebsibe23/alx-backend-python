#!/usr/bin/env python3
'''
This module contains a function called
'concat' that concatenates
two strings.

Usage Example:
result = concat("Hello, ", "world!")
print(result)  # Output: "Hello, world!"
'''


def concat(str1: str, str2: str) -> str:
    '''Concatenates two strings.'''
    try:
        return str1 + str2
    except TypeError:
        raise TypeError("Both 'str1' and 'str2' must be strings.")
