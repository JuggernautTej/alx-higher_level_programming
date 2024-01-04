#!/usr/bin/python3
import hidden_4
module_names = [name for name in dir(hidden_4) if not name.startswith("__")]
if __name__ == "__main__":
    for name in module_names:
        print("{}".format(name))
