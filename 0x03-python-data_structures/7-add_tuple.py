#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    tuple_a += (0, 0)
    tuple_b += (0, 0)
    tuple_sua = (tuple_a[0] + tuple_b[0])
    tuple_sub = (tuple_a[1] + tuple_b[1])
    tuple_sum = ()
    tuple_sum = (tuple_sua, tuple_sub)
    return tuple_sum
