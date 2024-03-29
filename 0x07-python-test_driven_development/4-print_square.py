#!/usr/bin/python3

"""module contain print_square"""


def print_square(size):
    """
    function that prints a square with the character #
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")

    for row in range(size):
        for column in range(size):
            print("#", end=(""))
        print()
