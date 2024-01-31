#!/usr/bin/python3
"""This function print_square takes in an integer as an argument
and prints a square with #.
"""


def print_square(size):
    """This function prints a square with the character #.
    Args:
    size (int): The first parameter

    Returns:
    Nothing.
    """
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not (isinstance(size, int)):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for z in range(size):
        print("#" * size)
