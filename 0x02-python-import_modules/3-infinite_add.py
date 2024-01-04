#!/usr/bin/python3
import sys
arguments = sys.argv[1:]
nos = len(arguments)
arg_ints = [int(arg) for arg in arguments]
result = sum(arg_ints)
if __name__ == "__main__":
    if nos == 1:
        print("{0}")
    else:
        print("{}".format(result))
