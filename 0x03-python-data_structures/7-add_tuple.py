#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0:
        res_a = (0, 0)
    elif len(tuple_a) == 1:
        res_a = (tuple_a[0], 0)
    elif len(tuple_a) > 2:
        res_a = (tuple_a[0], tuple_a[1])
    else:
        res_a = tuple_a
    if len(tuple_b) == 0:
        res_b = (0, 0)
    elif len(tuple_b) == 1:
        res_b = (tuple_b[0], 0)
    elif len(tuple_b) > 2:
        res_b = (tuple_b[0], tuple_b[1])
    else:
        res_b = tuple_b
    result = ((res_a[0] + res_b[0]), (res_a[1] + res_b[1]))
    return result
