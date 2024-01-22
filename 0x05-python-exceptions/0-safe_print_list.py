#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        y = 0
        for i in my_list[:x]:
            y += 1
            print("{}".format(i), end='')
    except IndexError:
        print("Index does't exist")
    finally:
        print()
    return y
