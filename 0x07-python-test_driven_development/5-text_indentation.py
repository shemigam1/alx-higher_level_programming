#!/usr/bin/python3

"""module contains text_indentation"""


def text_indentation(text):
    """
    function that prints a text with 2 new
    lines after each of these characters: ., ? and :
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    for delim in ".:?":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print("{}".format(text), end="")
