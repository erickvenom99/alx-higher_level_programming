#!/usr/bin/python3


import sys

if __name__ == "__main__":
    """Print the number of list arguments"""
    arguments = sys.argv[1:]
    num_arg = len(arguments)

    print("1 argument:" if num_arg == 1 else "Number of argument(s):",
          num_arg)

    if num_arg > 0:
        for i, arg in enumerate(arguments, start=1):
            print(i, ":", arg)
