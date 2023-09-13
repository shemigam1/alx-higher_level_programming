#!/usr/bin/python3
"""file description"""
import sys
import os
import json

"""Import the custom functions"""
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file


def main():
    """Check if the add_item.json file exists, and load its content if it does"""
    if os.path.isfile('add_item.json'):
        my_list = load_from_json_file('add_item.json')
    else:
        my_list = []

    # Add command-line arguments to the list
    my_list.extend(sys.argv[1:])

    # Save the updated list as a JSON representation in add_item.json
    save_to_json_file(my_list, 'add_item.json')


if __name__ == "__main__":
    """random docs"""
    main()
