#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    number_items = 0
    try:
        for i in range(x):
            print((my_list[i]), end="")
            number_items += 1
        print("")
    except:
        print("")
    return number_items
