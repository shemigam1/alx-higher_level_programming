#!/usr/bin/python3


"""
module contains class Base
"""


import json
import os


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

    @classmethod
    def save_to_file(cls, list_objs):
        """save to files method"""
        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".json"
        with open(filename, mode="w") as file:
            dict_list = [obj.to_dictionary() for obj in list_objs]
            json_str = cls.to_json_string(dict_list)
            file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """
        converts json string back to list of dictionaries
        """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """creates an instance"""
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        if cls.__name__ == 'Square':
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__ + '.json'
        l = []
        list_dicts = []
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                list_dicts = cls.from_json_string(f.read())
                for d in list_dicts:
                    l.append(cls.create(**d))
        return l
