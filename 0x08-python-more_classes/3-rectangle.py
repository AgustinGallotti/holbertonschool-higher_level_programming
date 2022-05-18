#!/usr/bin/python3
"""declare my class"""


class Rectangle:
    """coments to defiend"""

    def __init__(self, width=0, height=0):
        """rectangle for initialize"""
        self.width = width
        self.height = height

    @property
    def width(self):
        return (self.__width)

    @property
    def height(self):
        return (self.__height)

    @width.setter
    def width(self, width):
        """width setter"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @height.setter
    def height(self, height):
        """define the setter for the height"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        """define my area"""
        return (self.width * self.height)

    def perimeter(self):
        """define my perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        return self.height * 2 + self.width * 2

    def __str__(self):
        """define non-string"""
        if self.width == 0 or self.height == 0:
            return ""
        string = ""
        for i in range(self.height - 1):
            string += '#' * self.width + '\n'
        string += '#' * self.width
        return string
