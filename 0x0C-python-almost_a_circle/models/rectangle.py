#!/usr/bin/python3
"""module that creates a class called Rectangle that inherits from Base"""


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


class Rectangle(Base):
    """class Rectangle that inherits from Base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """class Constructor
        Attributes:
            width: Private instance attribute (integer)
            height: Private instance attribute (integer)
            x: Private instance attribute (integer), 0 by default
            y: Private instance attribute (integer, 0 by default
            id: Private instance attribute (integer) inherited from Base
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
