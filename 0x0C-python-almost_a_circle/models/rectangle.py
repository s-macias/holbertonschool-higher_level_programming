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

    @property
    def width(self):
        """ method for width value
        Return:
            width value: integer greater than 0
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter method for width
        Attribute:
            width value: must be an integer greater than zero
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ method for height value
        Return:
            height value: integer greater than 0
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter method for height

        Attribute:
            height value: must be an integer greater than zero
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ method for x value
        Return:
            x value: integer >= 0
        """
        return self.__x

    @x.setter
    def x(self, value):
        """ setter method for x

        Attribute:
            x value: must be an integer >= 0
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ method for y value
        Return:
            y value: integer >= 0
        """
        return self.__y

    @y.setter
    def y(self, value):
        """ setter method for y

        Attribute:
            y value: must be an integer >= 0
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ public method that calculates area
        Returns:
            area: integer
        """
        return self.width * self.height
