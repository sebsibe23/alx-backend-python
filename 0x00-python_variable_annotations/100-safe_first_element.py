#!/usr/bin/env python3
'''
This module contains a function
called 'safe_first_element' that
retrieves the first element of
a sequence if it exists.

Usage Example:
my_list = [1, 2, 3, 4, 5]
result = safe_first_element(my_list)
print(result)  # Output: 1
'''

from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''Retrieves the first element of
    a sequence if it exists.'''
    try:
        if lst:
            return lst[0]
        else:
            return None
    except IndexError:
        raise IndexError("The input must be a non-empty sequence.")
