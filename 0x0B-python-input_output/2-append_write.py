#!/usr/bin/python3

"""this module contains function append_write"""


def append_write(filename="", text=""):
    """appends text to a file"""
    with open(filename, 'a', encoding="utf-8") as f:
        f.append(text)
