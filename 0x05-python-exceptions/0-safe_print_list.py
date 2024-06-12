#!/usr/bin/python3
"""Modules defines a function that prints element in a list"""


def safe_print_list(my_list=[], x=0):
    count = 0
    for k in range(x):
        try:
            print(my_list[k], end="")
            count += 1
        except IndexError:
            break
    print()
    return (count)
