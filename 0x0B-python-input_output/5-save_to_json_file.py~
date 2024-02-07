#!/usr/bin/python3
"""This function that writes an object to a text file
using JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """This function that writes an object to a text file
    using JSON representation.
    Args:
        my_obj: the object to be written
        filename: the name of the file.
    Returns:
        None.
    """
    with open(filename, 'w', encoding= "utf-8") as txt_file:
        json.dump(my_obj, txt_file)
