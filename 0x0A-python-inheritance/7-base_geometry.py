#!/usr/bin/python3
"""This is class validates the values of a geometry"""


class BaseGeometry:
    """This is the geometry class."""
    def __init__(self):
        """This initializes the class"""
        pass

    def area(self):
        """This method raises an exceptio"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """This method valideates the value of the geometry"""
        if not (isinstance(value, int)):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
