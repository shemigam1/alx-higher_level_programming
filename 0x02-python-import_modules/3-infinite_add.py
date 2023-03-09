#!/usr/bin/python3
from sys import argv
range_of_vals = len(argv)
output = 0
for i in range(1, range_of_vals):
    output += int(argv[i])
print(output)
if __name__ == "__main__":
    3-infinite_add()
