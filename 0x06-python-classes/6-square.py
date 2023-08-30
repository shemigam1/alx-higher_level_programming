#!/usr/bin/python3

"""this module defines a class Square"""


class Square:
    """
    class square
    attributes:
        __size: int
    """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """getter for size"""
        return self.__size

    @property
    def position(self):
        """getter for position"""
        return self.__position

    @size.setter
    def size(self, value):
        """setter for size"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        """setter for position"""
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(val, int) for val in value) or \
           not all(val >= 0 for val in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0], "#" * self.__size)
