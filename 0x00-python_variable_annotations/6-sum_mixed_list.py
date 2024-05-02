#!/usr/bin/env python3
'''
This module contains a function
called 'sum_mixed_list' that computes
the sum of a list of integers
and floating-point numbers.

Usage Example:
mixed_numbers = [1, 2.5, 3, 4.7]
result = sum_mixed_list(mixed_numbers)
print(result)  # Output: 11.2
'''

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''Computes the sum of a list of integers
    and floating-point numbers.'''
    try:
        return float(sum(mxd_lst))
    except TypeError:
        raise TypeError("The input  must be a list of integers
                        and floating-point num.")
