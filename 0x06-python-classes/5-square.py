#!/usr/bin/python3

"""this module defines a class Square"""


class Square:
    """
    class square
    attributes:
        __size: int
    """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """getter for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter for size"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Description: returns the current area
        """
        return self.__size ** 2

    def my_print(self):
        """
        Description: prints in stdout the square with the character #
        """
        if self.__size == 0:
            print("")
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
