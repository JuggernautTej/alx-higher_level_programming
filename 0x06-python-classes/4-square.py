#!/usr/bin/python3
"""This defines the Square class"""


class Square:
    """This class has a private field entry."""
    def __init__(self, size=0):
        """
        Initializes the data
        Args:
        size (int): size of the square
        """
        self.__size = size

    @property
    def size(self):
        """a getter method"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area"""
        a = self.__size * self.__size
        return a
