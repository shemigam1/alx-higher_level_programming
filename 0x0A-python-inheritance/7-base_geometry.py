#!/usr/bin/python3

"""this module contains class BaseGeometry"""


class BaseGeometry:
    """class basegeometry"""
    def area(self):
        """calculates area"""
        raise Exception("area() is not implemented")

    def integer_validation(self, name, value):
        """validates value"""
        if not(isinstance(value, int)):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
