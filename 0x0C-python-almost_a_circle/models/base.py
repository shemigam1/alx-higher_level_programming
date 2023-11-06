#!/usr/bin/python3


"""
module contains class Base
"""


import json


class Base:
    """
    description: Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        init method
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        description: returns json representation
        of a list of dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    def save_to_file(cls, list_objs):
        """save to files method"""
        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".json"
        with open(filename, mode="w") as file:
            json_str = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
            file.write(json_str)
