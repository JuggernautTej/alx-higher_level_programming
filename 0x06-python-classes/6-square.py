#!/usr/bin/python3
"""This defines the Square class"""


class Square:
    """This class has two private field entries."""
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes the data
        Args:
        size (int): size of the square
        position (tuple): the position in the square
        """
        self.size = size
        self.__position = position

    @property
    def size(self):
        """a get/set method for size"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """a get/set method for the position tuple"""
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be of tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be of tuple of 2 positive integers")
        if not all(isinstance(x, int) for x in value):
            raise TypeError("position must be of tuple of 2 positive integers")
        if not all(x >= 0 for x in value):
            raise TypeError("position must be of tuple of 2 positive integers")

    def area(self):
        """Returns square area"""
        a = self.__size * self.__size
        return a

    def my_print(self):
        """Prints the square with the # character"""
        if self.__size == 0:
            print("")
        else:
            [print("") for x in range(0, self.__position[1])]
            for x in range(0, self.__size):
                [print(" ", end="") for y in range(0, self.__position[0])]
                [print("#", end="") for z in range(0, self.__size)]
                print("")
