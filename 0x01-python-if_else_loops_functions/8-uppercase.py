#!/usr/bin/python3
def uppercase(str):
    for x in str:
        if (ord(x) >= 97 or ord(x) <= 122):
            print("{}".format(x - 32))
        print("{}".format(x))
