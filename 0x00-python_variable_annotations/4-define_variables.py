#!/usr/bin/env python3
'''
This module assigns values to multiple variables.

Variables:
- a: an integer with a value of 1
- pi: a float with a value of 3.14
- i_understand_annotations: a boolean with a value of True
- school: a string with a value of 'Holberton'
'''


try:
    a: int = 1
    pi: float = 3.14
    i_understand_annotations: bool = True
    school: str = 'Holberton'
except Exception as e:
    print(f"An error occurred: {e}")
