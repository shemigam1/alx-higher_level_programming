#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_set = set()
    total = 0
    for i in my_list:
        if i not in my_set:
            my_set.add(i)
            total += i
    return total
