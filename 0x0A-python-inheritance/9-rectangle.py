#!/usr/bin/python3
"""Write a class Rectangle that inherits
    from BaseGeometry (7-base_geometry.py)."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Write a class Rectangle that inherits
        from BaseGeometry (7-base_geometry.py)."""

    def __init__(self, width, height):
        """ Inicialitation Rectangle
        Args:
            width (int): width
            height (int): height
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """the area() method must be implemented"""
        return self.__width * self.__height

    def __str__(self):
        """should print, and str() should return"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
