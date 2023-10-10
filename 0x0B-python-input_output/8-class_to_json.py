#!/usr/bin/python3

"""module contains function class_to_json"""


def class_to_json(obj):
    """converts class to json"""
    return obj.__dict__
