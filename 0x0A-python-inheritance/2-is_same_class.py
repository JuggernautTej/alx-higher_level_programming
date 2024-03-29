#!/usr/bin/python3
"""This function returns if an object is exactly an instance
of a specified class"""


def is_same_class(obj, a_class):
    """The function returns True if the object is an instance
    or False if otherwise.
    Args:
    obj: the object
    a_class: the class to check against.

    Returns:
    True or False.
    """
    return type(obj) == a_class
