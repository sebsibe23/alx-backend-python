#!/usr/bin/env python3
'''
This module contains a function called 'zoom_array' that creates
multiple copies of items in a tuple based on a given factor.

Usage Example:
array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)

print(zoom_2x)  # Output: [12, 12, 72, 72, 91, 91]
print(zoom_3x)  # Output: [12, 12, 12, 72, 72, 72, 91, 91, 91]
'''

from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    '''Creates multiple copies of items in a tuple.'''
    try:
        zoomed_in: List = [
            item for item in lst
            for _ in range(int(factor))
        ]
        return zoomed_in
    except TypeError:
        raise TypeError("The input 'lst' must be a tuple-like object.")
