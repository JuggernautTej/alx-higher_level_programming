#!/usr/bin/python3
"""This function say_my_name takes in two arguments, strings
and prints them.
"""


def say_my_name(first_name, last_name=""):
    """This function prints two strings in a sentence.
    Args:
    first_name (string): The first parameter
    last_name (string): The second parameter
    Returns:
    Nothing.
    """
    if not(isinstance(first_name, str)):
        raise TypeError("first_name must be a string")
    if not(isinstance(last_name, str)):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
