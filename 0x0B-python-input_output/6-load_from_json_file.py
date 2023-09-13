#!/usr/bin/python3
"""module contains function load_fom_json_file"""
import json


def load_from_json_file(filename):
    """creates an Object from a “JSON file”"""
    with open(filename, 'r', encoding="utf-8") as f:
        f_read = f.read()
        return json.loads(f_read)
