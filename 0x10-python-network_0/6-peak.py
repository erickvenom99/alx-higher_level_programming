#!/usr/bin/python3
"""
Finds the peak in an unordered list
"""


def find_peak(list_of_integers):
    """
    Functions find peak of unordered integers
    """
    if not list_of_integers:
        return None

    length = len(list_of_integers)
    if length == 0:
        return None
    elif length == 1:
        return list_of_integers[0]

    mid = length // 2
    peak = list_of_integers[mid]
    list_int = list_of_integers

    if peak > list_int[mid - 1] and peak > list_int[mid + 1]:
        return peak
    elif peak < list_int[mid - 1]:
        return find_peak(list_int[:mid])
    else:
        return find_peak(list_int[mid + 1:])
