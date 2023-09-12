#!/usr/bin/python3
from 7-base_geometry import BaseGeometry

"""this module contains class Rectangle"""


class Rectangle(BaseGeometry):
    """inherits from BaseGeometry"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
