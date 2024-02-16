#!/usr/bin/python3
"""This class define a square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """This class defines the methods and attributes for instances
    of a square."""
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes the data
        Args:
        size (int): the size of the square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """This sets the getter method for retrieving the
        size value and the setter method for setting
        it.
        """
        return self.width

    @size.setter
    def size(self, value):
        if not(isinstance(value, int)):
            raise TypeError("size must be an integer")
        if value <= 0:
            raise ValueError("size must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        """This returns a specific string"""
        return "[Square] ({}) {}/{} - {}".\
            format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """This method assigns arguments to each attribute"""
        attributes = ['id', 'size', 'x', 'y']
        for i in range(min(len(args), len(attributes))):
            setattr(self, attributes[i], args[i])
        if not args or len(args) == 0:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)

    def to_dictionary(self):
        """This method returns the dictionary represntation of a
        Square"""
        return {'id': self.id, 'x': self.x,
                'size': self.size, 'y': self.y}
