#!/usr/bin/python3
"""This defines a Square class"""


class Square:
    """This class has a private field entry."""
    def __init__(self, size=0):
        """
        Initializes the data
        Args:
        size (int): size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the current square area"""
        a = self.__size * self.__size
        return a
