#!/usr/bin/python3

"""module contains class Base"""


class Base:
    """
    class base
    """
    __nb_objects = 0
    def __init__(self, id=None):
        """init function"""
        if id is not None:
            self.id = id
        else:
            self.id = __nb_objects + 1
