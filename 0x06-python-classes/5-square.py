#!/usr/bin/python3
"""Write a class Square that defines a square"""


class Square:
    """optional initialization with size=0 which a positive int"""

    def __init__(self, size=0):
        """initilializes with size 0"""
        self._size = size

    @property
    def size(self):
        """method to retrieve size"""
        return size

    @size.setter
    def size(self, value):
        """method to set size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self._size = value

    def area(self):
        """method that returns area of the square"""
        return (self._size**2)

    def my_print(self):
        """method that prints a square"""
        if size is 0:
            print()
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print()
