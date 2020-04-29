#!/usr/bin/python3
if ord(c) >= 97 and ord(c) <= 122 and (ord(c) % 2) != 0:
    print("{:c}".format(ord(c) - 32), end="")
elif ord(c) >= 97 and ord(c) <= 122 and (ord(c) % 2) == 0:
    print("{:c}".format(ord(c), end=""))
