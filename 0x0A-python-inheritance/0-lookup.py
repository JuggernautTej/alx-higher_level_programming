#!/usr/bin/python3
"""This function returns the list of available attributes
and methods.
"""


def lookup(obj):
    """Returns the attributes of the object passed"""
    return dir(obj)
