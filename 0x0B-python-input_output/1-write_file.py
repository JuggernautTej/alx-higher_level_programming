#!/usr/bin/python3
"""This function writes a string to a text file and
returns the number of characters written"""


def write_file(filename="", text=""):
    """This function reads a string and returns
    the characters read.
    Args:
        filename: the name of the text file
        text (str): the string to be read
    Returns:
        characters read as an integer.
    """
    with open(filename, 'w', encoding="utf-8") as txt_file:
        chars_written = txt_file.write(text)
        return chars_written
