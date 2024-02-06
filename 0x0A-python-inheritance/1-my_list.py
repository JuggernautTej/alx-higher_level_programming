#!/usr/bin/python3
"""This class defines a rectangle as an empty class.
"""


class MyList(list):
    """This is a subclass."""
    def __init__(self, *args, **kwargs):
        """
        Initializes the instance of the class
        Args:
            None.
        """
        super().__init__(*args, **kwargs)

    def print_sorted(self):
        """This method prints the list in ascending order"""
        list_sorted = sorted(self)
        print(list_sorted)
