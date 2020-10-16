#!/usr/bin/python3
""" rectangle class """
from models.base import Base


class Rectangle(Base):
    """ rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """"inicialization constructor"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        """Call the super class with id"""
        super().__init__(id)

    @property
    def width(self):
        """Get and Set"""
        return self.__width

    @property
    def height(self):
        """Get and Set"""
        return self.__height

    @property
    def x(self):
        """Get and Set"""
        return self.__x

    @property
    def y(self):
        """Get and Set"""
        return self.__y

    @width.setter
    def width(self, value):
        """Set value
        Args:
            value (int): width of the rectangle
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Set value
        Args:
            value (int): height of the rectangle
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """Set value
        Args:
            value (int): x of the rectangle
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """Set value
        Args:
            value (int): y of the rectangle
        """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area value of the Rectangle"""
        return self.__width * self.__height

    def display(self):
        """prints in stdout the Rectangle"""
        print(("\n" * self.__y) +
              "\n".join(((" " * self.__x) + ("#" * self.__width))
                        for i in range(self.__height)))

    def __str__(self):
        """should print, and str() should return"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += "(" + str(self.id) + ") " + \
            str(self.__x) + "/" + str(self.__y) + " - " + \
            str(self.__width) + "/" + str(self.__height)
        return string

    def update(self, *args, **kwargs):
        """update"""
        for i, j in enumerate(args):
            if i == 0:
                self.id = j
            elif i == 1:
                self.width = j
            elif i == 2:
                self.height = j
            elif i == 3:
                self.x = j
            elif i == 4:
                self.y = j
        if "id" in kwargs:
            self.id = kwargs["id"]
        if "width" in kwargs:
            self.width = kwargs["width"]
        if "height" in kwargs:
            self.height = kwargs["height"]
        if "x" in kwargs:
            self.x = kwargs["x"]
        if "y" in kwargs:
            self.y = kwargs["y"]

    def to_dictionary(self):
        """to_dictionary"""
        dic = {}
        dic["id"] = self.id
        dic["width"] = self.width
        dic["height"] = self.height
        dic["x"] = self.x
        dic["y"] = self.y
        return dic
