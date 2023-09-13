#!/usr/bin/python3

"""module contains function class_to_json"""


def class_to_json(obj):
    """converts class to json"""
    serialized_dict = {}
    attributes = dir(obj)
    for attr_name in attributes:
        attr_value = getattr(obj, attr_name)
        if isinstance(attr_value, (list, dict, str, int, bool)):
            serialized_dict[attr_name] = attr_value
    return serialized_dict
