#!/usr/bin/python3
"""
this module contains function to_json_string
"""
import json


def to_json_string(my_obj):
    """returns json representation of object"""
    return json.dumps(my_obj)
