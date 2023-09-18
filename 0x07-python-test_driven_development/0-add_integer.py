#!/usr/bin/python3

"""module containing function add_integer"""


def add_integer(a, b=98):
    """
    Description: a module that adds 2 integers
    """
    if not (isinstance(a, (int, float))):
        raise TypeError("a must be an integer")
    if not (isinstance (b, (int, float))):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b

    if __name__ == "__main__":
        import doctest
        doctest.testfile("tests/0-add_integer.txt")
