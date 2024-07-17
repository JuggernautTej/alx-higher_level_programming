#!/usr/bin/python3
"""This class defines a rectangle with its area, perimeter and hash tag
represention.
"""


class Rectangle:
    """This is not an empty class but defines the area and perimeter of
    a rectangle instance.
    """
    def __init__(self, width=0, height=0):
        """
        Initializes the instance of the class
        Args:
        width (int): the width of the rectangle
        height (int): the height of the rectangle
        """
        if not (isinstance(width, int)):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not (isinstance(height, int)):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """This sets the getter and setter methods for the rectangle width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not (isinstance(value, int)):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """This sets the getter method for retrieving the height value and the
        setter method for setting the rectangle height.
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not (isinstance(value, int)):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """This method returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """This method returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            p = 0
        else:
            p = (self.__height * 2) + (self.__width * 2)
        return p

    def __str__(self):
        """The method to return the rectangle as a human readable string using
        the # character.
        """
        result = ''
        if self.__width == 0 or self.__height == 0:
            return result
        else:
            for column in range(self.__height):
                for row in range(self.__width):
                    result += "#"
                if column < self.__height - 1:
                    result += "\n"
            return result

    def __repr__(self) -> str:
        """This returns a string representation of the rectangle to be
        able to recreate a new instance by using eval function"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """This method is called when an instance of the class is about
        to be destroyed"""
        print("Bye rectangle...")
