#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        y = 0
        for i in my_list[:x]:
            if isinstance(i, int):
                y += 1
                print("{:d}".format(i), end='')
    except IndexError:
        print("IndexError: list out of range")
    finally:
        print()
    return y
