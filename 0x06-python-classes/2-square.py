#!/usr/bin/python3
"""program that creates the class Square with optinal attribute size"""


class Square:
    """size must be an integer (TypeError) and greater than 0 (ValueError)"""

    def __init__(self, size=0):
        try:
            self._size = size
        except (TypeError):
            print("size must be an integer")
        except (ValueError):
            print("size must be >= 0")
