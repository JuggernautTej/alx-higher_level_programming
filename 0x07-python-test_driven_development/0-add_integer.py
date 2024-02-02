#!/usr/bin/python3
"""This houses the add_integer function along with its definition"""


def add_integer(a, b=98):
    """This function takes two args, either integers or floats, and
    returns the sum of both as an integer.

    Args:
    a (int or float): The first argument.
    b (98, int or float): The second argument.

    Returns:
    Sum.

    """
    if not (isinstance(a, (int, float)) and a is not None):
        raise TypeError("a must be an integer")
    if not (isinstance(b, (int, float)) and b is not None):
        raise TypeError("b must be an integer")
    result = a + b
    max_float = 1.8e308
    min_float = -1.8e308
    if result > max_float or result < min_float:
        raise OverflowError
    return int(result)
