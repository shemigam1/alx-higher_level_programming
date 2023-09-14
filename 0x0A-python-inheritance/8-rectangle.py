#!/usr/bin/python3

"""this module contains class baseGeometry"""

class BaseGeometry:
    """class basegeometry"""
    def area(self):
        """calculates area"""
        raise Exception("area() is not implemented")

    def integer_validation(self, name, value):
        """validates value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """inherits from BaseGeometry"""
    def __init__(self, width, height):
        """initialize class Rectangle"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
