#!/usr/bin/python3
"""returns the number of lines of a text file"""


def number_of_lines(filename=""):
    """returns the number of lines of a text file

    Args:
        filename: file whose lines will be counted

    Returns:
        number of lines
    """
    with open(filename, encoding="utf-8") as myFile:
        nb_lines = 1
        while True:
            line = myFile.readline()
            if not line:
                break
            nb_lines += 1
        print(nb_lines)
