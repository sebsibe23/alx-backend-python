#!/usr/bin/env python3
'''
This module contains a function
called 'sum_list' that computes
the sum of a list of floating-point numbers.

Usage Example:
numbers = [1.5, 2.7, 3.9]
result = sum_list(numbers)
print(result)  # Output: 8.1
'''

from typing import List


def sum_list(input_list: List[float]) -> float:
    '''Computes the sum of a list of
    floating-point numbers.'''
    try:
        return float(sum(input_list))
    except TypeError:
        raise TypeError("The input must be a list of floating-point numbers.")
