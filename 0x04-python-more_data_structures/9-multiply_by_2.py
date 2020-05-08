#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    for x, y in a_dictionary.items():
        a_dictionary[x] *= 2
    new_dic = a_dictionary.copy()
    return new_dic
