#!/usr/bin/python3


if __name__ == "__main__":
    """Module defines number of args on command-line"""
    import sys

    num = len(sys.argv) - 1
    if num == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(num))
    for i in range(num):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
