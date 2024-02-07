#!/usr/bin/python3
"""This function creates an object from
a JSON file"""
import json


def load_from_json_file(filename):
    """This function creates an object from a JSON file
    Args:
        filename: the name of the file.
    Returns:
        Nothing
    """
    with open(filename, 'r', encoding="utf-8") as txt_file:
        contents = json.load(txt_file)
        return contents
