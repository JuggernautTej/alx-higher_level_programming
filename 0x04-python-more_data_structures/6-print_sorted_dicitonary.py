#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_sort = sorted(a_dictionary.items())
    for key, value in new_sort:
        print("{}: {}".format(key, value))
