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
        while True:
            line = myFile.readline()
            nb_lines += 1
            if not line:
                break
        print(nb_lines)
