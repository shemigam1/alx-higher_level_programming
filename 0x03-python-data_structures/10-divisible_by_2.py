#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    cpy = [x % 2 == 0 for x in my_list]
    return cpy
