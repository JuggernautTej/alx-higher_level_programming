#!/usr/bin/python3
"""This class defines a base class.
"""
import json


class Base:
    """This is an interesting class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes the instance of the class
        Args:
            id (int): the identification number
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """This is a static method that returns
        the JSON representation of an object
        """
        json_rep = json.dumps(list_dictionaries)
        return json_rep
