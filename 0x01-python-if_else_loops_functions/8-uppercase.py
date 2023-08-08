#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if 'a' <= i <= 'z':
            offset = ord('A') - ord('a')
            print("{}".format(chr(ord(i) + offset)), end="")
        else:
            print(i, end="")
    print()
