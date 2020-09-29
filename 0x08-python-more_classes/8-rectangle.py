#!/usr/bin/python3
""" Write a class Rectangle that defines
    a rectangle by: (based on 0-rectangle.py) """


class Rectangle:
    """ Write a class Rectangle that defines
        a rectangle by: (based on 0-rectangle.py) """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Inizialitation
        Args:
            width (int): Private instance attribute: width.
            height (int): Private instance attribute: height.
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get and Set"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set value
        Args:
            value (int): width of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get and Set"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set value
        Args:
            value (int): height of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ return the area
        Returns:
            the return value is the area
        """
        return self.__width * self.__height

    def perimeter(self):
        """ return the perimeter
        Returns:
            the return value is the perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """ should print the rectangle with the character
        #: (see example below)
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rectangle = []
        for i in range(self.__height):
            [rectangle.append(str(self.print_symbol))
                for j in range(self.__width)]
            if i is not self.__height - 1:
                rectangle.append("\n")
        return ("".join(rectangle))

    def __repr__(self):
        """return a string representation of the rectangle to be able
        to recreate a new instance by using eval() (see example below)
        """
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """Print the message Bye rectangle...
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area
        Args:
            rect_1 (Rectangle): rectangle 1
            rect_2 (Rectangle): rectangle 2
        Raises:
        Returns:
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)
