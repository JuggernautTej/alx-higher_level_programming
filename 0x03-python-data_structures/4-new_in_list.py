#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """A function the replaces a list element at a specific position
    without modifying the original list"""
    temp_list = my_list[:]
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        temp_list[idx] = element
        return temp_list
