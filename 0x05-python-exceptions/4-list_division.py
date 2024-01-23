#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for z in range(list_length):
        try:
            x = my_list_1[z]
            y = my_list_2[z]
            result.append(x / y)
        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
        except (TypeError, ValueError):
            print("wrong type")
            result.append(0)
        except IndexError:
            print("out of range")
            result.append(0)
        finally:
            result *= 1
    return result
