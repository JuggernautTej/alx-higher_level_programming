#!/usr/bin/python3
"""This function returns if an object is an instance
of or the object is an instance of a class"""


def is_kind_of_class(obj, a_class):
    """The function returns True if the object is an instance
    or False if otherwise.
    Args:
    obj: the object
    a_class: the class to check against.

    Returns:
    True or False.
    """
    return isinstance(obj, a_class)
