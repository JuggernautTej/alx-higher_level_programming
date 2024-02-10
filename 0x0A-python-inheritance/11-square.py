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

    def area(self):
        """This class returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """This returns a specific string"""
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """This class defines the methods and attributes for instances
    of a square."""
    def __init__(self, size):
        """
        Initializes the data
        Args:
        size (int): the size of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """This method defines the area of a square"""
        return self.__size ** 2

    def __str__(self):
        """This returns a specific string"""
        return f"[Square] {self.__size}/{self.__size}"
