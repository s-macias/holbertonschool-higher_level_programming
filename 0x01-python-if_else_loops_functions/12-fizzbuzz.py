#!/usr/bin/python3
def fizzbuzz():
    for n in range(1, 101):
        if n % 3:
            print("Fizz ", end="")
        elif n % 5:
            print("Buzz ", end="")
        elif n % 3 and n % 5:
            print("FizzBuzz ", end="")
        else:
            print("{:d} ".format(n), end="")
