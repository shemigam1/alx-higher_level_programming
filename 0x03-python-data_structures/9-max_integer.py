#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)
    i = 0
    max = my_list[i]
    for num in my_list:
        if num > max:
            max = num
    return max
