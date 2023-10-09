#!/usr/bin/python3

"""this module contains class baseGeometry"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """inherits from Rectangle"""
    def __init__(self, size):
        """initialization"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """calculates area"""
        return self.__size ** 2
