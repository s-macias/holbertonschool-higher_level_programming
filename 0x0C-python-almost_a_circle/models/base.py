#!/usr/bin/python3
"""module that creates a class called Base"""


class Base:
    """This class will be the “base” of all other classes in this project.
    Its goal is to manage the id attribute in all your future classes and
    to avoid duplicating the same code.

    Attributes:
        __nb_objects = 0: private class attribute
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """"class constructor
        Attributes:
            id: integer, public instance attribute
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
