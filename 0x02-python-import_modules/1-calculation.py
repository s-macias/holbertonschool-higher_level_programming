#!/usr/bin/python3
from calculator_1 import add, sub, mul, div


if __name__ == "_main__":
    a = 1
    b = 5
    print("{:d} +  {:d} = {:d}".format(a, b, add(a, b)))
    print("{:d} -  {:d} = {:d}".format(a, b, sub(a, b)))
    print("{:d} *  {:d} = {:d}".format(a, b, mul(a, b)))
    print("{:d} /  {:d} = {:d}".format(a, b, div(a, b)))
