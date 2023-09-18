#!/usr/bin/python3

"""module contains class Square"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """init method"""
        self.__size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """str method"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
