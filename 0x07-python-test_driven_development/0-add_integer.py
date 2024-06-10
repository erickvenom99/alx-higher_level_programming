#!/usr/bin/python

def add_integer(a, b=98):
    """
    Sums arguments a and b.

    Args:
         a (float or int): First argument.
         b (float or int, optional): Second argument. Defaults to 98.

    Returns:
            int: Sum of a and b, casted to an integer.

    Raises:
          TypeError: If a or b is not an integer or float.

    Examples:
            >>> add_integer(5, 0.9)
            5
            >>> add_integer(0.4, 6)
            6
            >>> add_integer(4, 6)
            10

    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    result = a + b
    return (result)
