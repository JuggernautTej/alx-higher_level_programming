#!/usr/bin/python3
import sys
arguments = sys.argv
nos = len(arguments)
if __name__ == "__main__":
    if nos == 1:
        print("0 arguments.")
    elif nos == 2:
        print("1 argument:\n1: {}".format(arguments[1]))
    else:
        print("{} arguments:".format(nos - 1))
        for i in range(nos - 1):
            print("{}: {}".format(i + 1, arguments[i + 1]))
