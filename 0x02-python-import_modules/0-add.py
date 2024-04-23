#!/usr/bin/python3


if __name__ == "__main__":
    """Module defines an addition operation"""

    from add_0 import add
    a = 1
    b = 2
    result = add(a, b)
    print("{} + {} = {}".format(a, b, add(a, b)))
