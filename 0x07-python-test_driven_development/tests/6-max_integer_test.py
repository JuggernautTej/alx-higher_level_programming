#!/usr/bin/python3
"""This function text_indentation prints a text with 2 lines
after each of these characters: . , ? and :
"""


import unittest
max_integer = __import__('6_max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ This is a class for testing the max_integer function
    through the unittest module.
    Attributes:
    No class attributes.
    """
    def test_max(self):
        """This function tests the max function using
        different cases.
        Args:
        None.
        Returns:
        Nothing.
        """
        self.assertEqual(max_integer([2, 3, 10, 400]), 400)
        self.assertEqual(max_integer([3]), 3)
        self.assertEqual(max_integer([1.38, 7.98, 9.74]), 9.74)
        self.assertEqual(self.max3, None)
        with self.assertRaises(TypeError):
            max_integer([3, 4, 'dear'])


if __name__ == "__main__":
    unittest.main()
