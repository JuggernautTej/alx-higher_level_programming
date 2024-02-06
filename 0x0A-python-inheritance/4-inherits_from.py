#!/usr/bin/python3
"""This function returns a boolean depending on if the object
is an instance of a class that inherited from the said class
"""


def inherits_from(obj, a_class):
    """The function returns True if the object is an instance
    of a class that inherited from the said class
    or False if otherwise.
    Args:
    obj: the object
    a_class: the class to check against.

    Returns:
    True or False.
    """
    class_obj = type(obj)
    while class_obj is not None:
        if issubclass(class_obj, a_class):
            return True
        class_obj = class_obj.__base__
    retuen False
