#!/usr/bin/python3
def common_elements(set_1, set_2):
    final = []
    for i in set_1:
        if i in set_2:
            final.append(i)
    return final

