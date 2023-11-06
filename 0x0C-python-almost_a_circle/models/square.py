#!/usr/bin/python3


"""
module contains class Square
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    description: class Rectangle inherits from
    class Rectangle which inherits from class Base
    """
    def __init__(self, size, x=0, y=0, id=None):
        """init method"""
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """str method"""
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter for size"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value
