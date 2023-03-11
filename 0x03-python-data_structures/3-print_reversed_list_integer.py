#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    rev_list = my_list[::-1]
    for list in range(len(my_list)):
        print("{:d}".format(rev_list[list]))
