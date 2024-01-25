#!/usr/bin/python3
"""This defines the Square class."""


class Square:
    """This class has a private field entry."""
    def __init__(self, size):
        """
        Initializes the data
        Args:
        size (int): size of the square.
        """
        self.__size = size

    @property
    def size(self):
        """Get/set the current size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else.__size = value

    def area(self):
        """Returns the current square area."""
        a = self.__size * self.__size
        return a

    def my_print(self):
        """Prints # based on the value of size"""
        if self.__size == 0:
            print("")
        else:
            for x in range(self.__size):
                print("#" * self.__size)
