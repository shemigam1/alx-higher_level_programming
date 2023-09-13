#!/usr/bin/bash

"""module contains function class_to_json"""


def class_to_json(obj):
    """converts class to json"""
    serialized_dict = {}

    # Get a list of all attributes of the object
    attributes = dir(obj)

    # Iterate through the attributes and serialize those that are serializable
    for attr_name in attributes:
        attr_value = getattr(obj, attr_name)

        # Check if the attribute is of a serializable data type
        if isinstance(attr_value, (list, dict, str, int, bool)):
            serialized_dict[attr_name] = attr_value

    return serialized_dict
