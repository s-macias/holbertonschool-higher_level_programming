#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    number_items = 0
    try:
        for i in range(x):
            print("{:d}".format(my_list[i]), end="")
            number_items += 1
    except (TypeError, ValueError):
        pass
    return number_items
