#!/usr/bin/python3
"""This function returns object representation of
a JSON string"""
import json


def from_json_string(my_str):
    """This function returns object representation of
    a JSON string.
    Args:
        my_str(json): the json
    Returns:
        Object representation.
    """
    obj_string = json.loads(my_str)
    return obj_string
