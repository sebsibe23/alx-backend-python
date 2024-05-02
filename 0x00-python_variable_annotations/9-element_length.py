#!/usr/bin/env python3
'''
This module contains a function 
called 'element_length' that computes
the length of each sequence in 
a list of sequences.

Usage Example:
sequences = ["apple", (1, 2, 3), [4, 5, 6], "banana"]
result = element_length(sequences)
print(result)  # Output: [('apple', 5), 
((1, 2, 3), 3), ([4, 5, 6], 3), ('banana', 6)]
'''

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''Computes the length of each 
    sequence in a list of sequences.'''
    try:
        return [(i, len(i)) for i in lst]
    except TypeError:
        raise TypeError("The input 'lst' must be an iterable of sequences.")
