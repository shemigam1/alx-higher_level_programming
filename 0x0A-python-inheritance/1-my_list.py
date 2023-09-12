#!/usr/bin/python3

"""this module defines a class MyList"""


class MyList(list):
    """
    class MyList
    """
    def print_sorted(self):
        """prints sorted list"""
        sorted_list = sorted(self)
        print(sorted_list)
