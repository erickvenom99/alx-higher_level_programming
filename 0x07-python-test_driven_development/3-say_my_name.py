#!usr/bin/python3
"""
Module prints a name
"""


def say_my_name(first_name, last_name=""):
    """
    Function that prints my name.

    Args:
        first_name (str): First name.
        last_name (str, optional): Last name or an empty string.
        Defaults to an empty string.

    Raises:
        TypeError: If first_name or last_name is not a string.

    Examples:
        >>> say_my_name("Alice", "Trice")
        My name is Alice Trice
        >>> say_my_name("Alice")
        My name is Alice
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if last_name:
        print("My name is {} {}".format(first_name, last_name))
    else:
        print("My name is {}".format(first_name))
