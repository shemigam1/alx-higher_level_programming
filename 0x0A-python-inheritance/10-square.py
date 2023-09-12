#!/usr/bin/python3

"""this module contains class baseGeometry"""


class BaseGeometry:
    """class basegeometry"""
    def area(self):
        """area method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """int valudation for value"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


"""this module contains class Rectangle"""


class Rectangle(BaseGeometry):
    """inherits from BaseGeometry"""
    def __init__(self, width, height):
        """initialize class Rectangle"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """calc area"""
        return self.__width * self.__height

    def __str__(self):
        """string representation of class"""
        return f"[Rectangle] {self.__width}/{self.__height}"


"""this module contains class Square"""


class Square(Rectangle):
    """inherits from Rectangle"""
    def __init__(self, size):
        """initialization"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """calculates area"""
        return self.__size ** 2
