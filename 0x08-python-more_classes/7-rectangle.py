#!/usr/bin/python3

"""this module defnes a class rectangle"""


class Rectangle:
    """
    class Rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Description: returns the current area
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Description: returns the current perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width) + (2 * self.__height)

    def __str__(self):
        """
        Description: str function
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle_str = ""
        return str(self.print_symbol) * self.__width + "\n" + \
               (str(self.print_symbol) * self.__width + "\n") * (self.__height - 1) + \
               str(self.print_symbol) * self.__width

    def __repr__(self):
        """Description: repr method"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """delete method"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
