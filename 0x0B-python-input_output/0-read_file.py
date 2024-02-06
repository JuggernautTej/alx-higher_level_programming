#!/usr/bin/python3
"""This function opens a file to be read and
prints its contents"""


def read_file(filename=""):
    """This function prints the contents of a text file

    Args:
        filename: the name of the text file.
    Returns:
        Nothing
    """
    with open(filename, 'r', encoding="utf-8") as txt_file:
        contents = txt_file.read()
        print(contents, end='')
