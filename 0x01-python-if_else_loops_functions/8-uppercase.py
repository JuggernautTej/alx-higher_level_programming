#!/usr/bin/python3
def uppercase(str):
    """Prints a string in uppercase followed by a newline"""
    result = ""
    for char in str:
        if 'a' <= char <= 'z':
            upper_time = chr(ord(char) - ord('a') + ord('A'))
            result += upper_time
        else:
            result += char
    print("{}".format(result))
