#!/usr/bin/python3
"""This class defines a student"""


class Student:
    """This class has all its attributes as public instances"""
    def __init__(self, first_name, last_name, age):
        """
        Initializes the data
        Args:
            first_name (str): the first name of the student
            last_name (str): the student last name
            age (int): The student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """This function returns the dictionary description
        with simple data structure for JSON serialization of
        an object
        Args:
        self: the data structure
        Returns:
        A dictionary description.
        """
        if isinstance(self, (int, float, str, bool, type(None))):
            return self
        elif isinstance(self, list):
            return [item.to_json() if isinstance(item, Student)
                    else item for item in self]
        elif isinstance(self, dict):
            return {key: value.to_json() if isinstance(value, Student)
                    else value for key, value in self.items()
                    for key, value in self.items()}
        else:
            return {key: value.to_json() if isinstance(value, Student)
                    else value for key, value in vars(self).items()
                    for key, value in vars(self).items()}
