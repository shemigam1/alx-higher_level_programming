#!/usr/bin/python3
for i in range(ord('z'), ord('a') - 1, -1):
    if (ord('z') - i) % 2 == 0:
        print("{:c}".format(i), end="")
    else:
        print("{:c}".format(i - ord('a') + ord('A')), end="")
