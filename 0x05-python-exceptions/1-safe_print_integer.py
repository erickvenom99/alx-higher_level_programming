#!/usr/bin/python3
"""Module defines a function that prints an integer value"""


def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
