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

    def update(self, *args, **kwargs):
        """update method"""
        if args is not None and len(args) != 0:
            if lens(args) >= 1:
                if type(args[0]) != int and args[0] is not None:
                    raise TypeError("id must be an integer")
            self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if lens(args) > 2:
                self.x = args[2]
            if lens(args) > 3:
                self.y = args[3]
        else:
            for key, val in kwargs.items():
                if key == 'id':
                    if type(val) != int and val is not None:
                        raise TypeError("id must be an integer")
                    self.id = val
                if key == 'size':
                    self.size = val
                if key == 'x':
                    self.x = val
                if key == 'y':
                    self.y = val

    def to_dictionary(self):
        """returns dictionary representation"""
        return {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
                }
