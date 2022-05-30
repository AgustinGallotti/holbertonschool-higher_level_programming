#!/usr/bin/python3
"""Implement a rectangle class from basegeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class based on BaseGeometry"""

    def __init__(self, width, height):
        """we initialize"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """return area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Return information about rectangle in string format"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
