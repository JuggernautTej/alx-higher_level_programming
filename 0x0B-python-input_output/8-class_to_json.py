#!/usr/bin/python3
"""This function returns the dictionary description with simple
data structure for JSON serialization of an object"""


def class_to_json(obj):
    """This function returns the dictionary description
    with simple data structure for JSON serialization of
    an object
    Args:
        obj: the data structure
    Returns:
        A dictionary description.
    """
    if isinstance(obj, (int, float, str, bool, type(None))):
        return obj
    elif isinstance(obj, list):
        return [class_to_json(item) for item in obj]
    elif isinstance(obj, dict):
        return {key: class_to_json(value) for key, value in obj.items()}
    else:
        return {key: class_to_json(value) for key, value in vars(obj).items()}
