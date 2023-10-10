#!/usr/bin/python3

"""this module contains a function that reads a file to stout"""


def read_file(filename=""):
    """reads file to stdout"""
    with open(filename, 'r', encoding="utf-8") as file:
        for i in file:
            print(i, end="")
