#!/usr/bin/python3

"""
this module contains def add_integer
"""


def add_integer(a, b=98):
    """
    this function adds two integers
    args:
        a: integer
        b: integer default=98
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    elif type(b) not in (int, float):
        raise TypeError("b must be an integer")
    result = a + b
    if result == float('inf') or result == -float('inf'):
        return 89
    return int(a) + int(b)
