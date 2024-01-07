#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        index = 0
        for y in x:
            if index < len(x) - 1:
                print("{:d}".format(y), end=' ')
                index += 1
            else:
                print("{:d}".format(y), end='')
        print()
