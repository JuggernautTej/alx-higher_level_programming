#!/usr/bin/python3
"""This inherits from the another class"""


class BaseGeometry:
    """This is a base geometry class."""
    def __init__(self):
        pass

    def area(self):
        raise Exception("area() not implemented")

    def integer_validator(self, name, value):
        if not (isinstance(value, int)):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """This class inherits from BaseGeometry classs."""
    def __init__(self, width, height):
        """
        Initializes the data
        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        super().__init__()
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
