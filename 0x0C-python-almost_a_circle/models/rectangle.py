#!/usr/bin/python3
"""This class defines a rectangle as class.
"""
from models.base import Base


class Rectangle(Base):
    """This is class inherits from the Base parent class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes the instance of the class
        Args:
        width (int): the width of the rectangle
        height (int): the height of the rectangle
        x (int): the x coordinate of the rectangle's starting point.
        y (int): the y coordinate of the rectangle's starting point.
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """This sets the getter and setter methods"""
        return self.__width

    @width.setter
    def width(self, value):
        if not(isinstance(value, int)):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """This sets the getter method for retrieving the
        height value and thw setter method for setting the
        rectangle height.
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not(isinstance(value, int)):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """This sets the getter method for retrieving the
        x cordinate value and the setter method for setting
        it.
        """
        return self.__x

    @x.setter
    def x(self, value):
        if not(isinstance(value, int)):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """This sets the getter method for retrieving the
        y cordinate value and the setter method for setting
        it.
        """
        return self.__y

    @y.setter
    def y(self, value):
        if not(isinstance(value, int)):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculates the area of the rectangle."""
        return self.__width * self.__height

    def display(self):
        """This method prints in the stdout the
        rectangle instance using the '#' character"""
        result = ''
        if self.__width == 0 or self.__height == 0:
            print(result, end='')
        else:
            for z in range(self.__y):
                result += '\n'
            for i in range(self.__height):
                result += (' ' * self.__x) + ('#' * self.__width) + '\n'
            print(result, end='')

    def __str__(self):
        """This returns a specific string"""
        return "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """This method assigns an argument to each attribute"""
        args_nos = len(args)
        if args_nos > 0:
            self.id = args[0]
        if args_nos > 1:
            self.__width = args[1]
        if args_nos > 2:
            self.__height = args[2]
        if args_nos > 3:
            self.__x = args[3]
        if args_nos > 4:
            self.__y = args[4]
        for key, value in kwargs.items():
            if key == 'id':
                self.id = value
            if key == 'width':
                self.__width = value
            if key == 'height':
                self.__height = value
            if key == 'x':
                self.__x = value
            if key == 'y':
                self.__y = value
