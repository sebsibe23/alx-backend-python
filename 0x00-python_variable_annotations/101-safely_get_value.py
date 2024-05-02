#!/usr/bin/env python3
'''
This module contains a function called
'safely_get_value' that retrieves
a value from a dictionary using a given
key and returns a default value
if the key does not exist.

Usage Example:
my_dict = {'a': 1, 'b': 2, 'c': 3}
result1 = safely_get_value(my_dict, 'b')
result2 = safely_get_value(my_dict, 'd', default=0)
print(result1)  # Output: 2
print(result2)  # Output: 0
'''

from typing import Any, Mapping, Union, TypeVar


T = TypeVar('T')
Res = Union[Any, T]
Def = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    '''Retrieves a value from a dictionary
    using a given key.'''
    try:
        if key in dct:
            return dct[key]
        else:
            return default
    except TypeError:
        raise TypeError("The input 'dct' must be a dictionary-like object.")
