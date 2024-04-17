#!/usr/bin/python3
"""Module defines an inherited list class MyList."""


class MyList(list):
    """Execurtes a sorted print for the built-in list class."""


def print_sorted(self):
    """print a list in ascending order"""
    print(sorted(self))
