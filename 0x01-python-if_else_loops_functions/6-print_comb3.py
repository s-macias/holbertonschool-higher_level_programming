#!/usr/bin/python3
for number in range(0, 9):
    for number2 in range(0, 10):
        if number < number2:
            if number * 10 + number2 != 89:
                print("{:d}{:d}".format(number, number2, end=""))
        elif number * 10 + number2 is 89:
            print("{:d}{:d}".format(number, number2))
