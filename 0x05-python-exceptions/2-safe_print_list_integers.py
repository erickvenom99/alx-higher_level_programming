#!/usr/bin/python3
"""Module prints the first integer element on a list """

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for k in range(0, x):
            if isinstance(my_list[k], int):
                print("{:d}".format(my_list[k]), end=" ")
                count += 1
    except(IndexError, ValueError, TypeError):
        continue
    print()
    return count
