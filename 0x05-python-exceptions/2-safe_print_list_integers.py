#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    number_items = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            number_items += 1
        except (TypeError, ValueError):
            pass
    print()
    return number_items
