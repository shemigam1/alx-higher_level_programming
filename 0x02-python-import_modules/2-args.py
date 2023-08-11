#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = len(sys.argv) - 1

    if i == 0:
        print("{} arguments.".format(i))
    elif i == 1:
        print("{} arguments:".format(i))
    else:
        print("{} arguments:".format(i))

    if i >= 1:
        for i in range(1, len(sys.argv)):
            print("{}: {}".format(i, sys.argv[i]))
