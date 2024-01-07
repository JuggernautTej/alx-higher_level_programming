#!/usr/bin/python3
def no_c(my_string):
    str_list = list(my_string)
    chr_to_remove = ["c", "C"]
    for chr in chr_to_remove:
        str_list = [str for str in str_list if str != chr]
    return ''.join(str_list)
