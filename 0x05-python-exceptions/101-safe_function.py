#!/usr/bin/python3
"""Module execute a function safely"""


import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
        return (result)
    except Exception as i:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
