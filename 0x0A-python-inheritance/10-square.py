#!/usr/bin/python3
"""class square"""
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """my square"""

    def __init__(self, size=0):
        """area of the rectangle"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """area of the rectangle"""
        return self.__size ** 2

    def __str__(self):
        """print, super ignore my def str in rect"""
        return super().__str__()
