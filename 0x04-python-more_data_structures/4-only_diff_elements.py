#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    total = []
    for i in set_1:
        if i not in set_2:
            total.append(i)
    for j in set_2:
        if j not in set_1:
            total.append(j)
    return total
