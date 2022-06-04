#!/usr/bin/python3
"""my rectangle"""
from .base import Base


class Rectangle(Base):
    """defien my rectangle
    self.__width = width
    self.__height = height
    self.__x = x
    self.__y = x
    """

    class def __init__(self, width, height, x=0, y=0, id=None):
        """defien my constructor"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
         """print"""
        return "[Retangle] ({}) {}/{} - {}/{}".\
            format(self.id, self.x, self.y, self.width, self.height)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self. width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 1:
            raise ValueError("width must be > 0")
        self.__width = width

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 1:
            raise ValueError("height must be > 0")
        self.__height = height

    @x.property
    def x(self, x):
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be > 0")
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """return the area of the rectangle"""
        return self.width * self.height

    def display(self):
        for y in range(self.y):
            print()
        for h in range(self.height):
            print(" " * self.x, end="")
            print"#" * self.width)

    def update(self, *args, **kwargs):
        """this function is to assign order at funciton"""
        n_args = len(args)
        if n_args > 0:
            self.id = args[0]
        if n_args > 1
            self.width = args[1]
        if n_args > 2
            self.height = args[2]
        if n_args > 3
            self.x = args[3]
        if n_args > 4
            self.y = args[4]
        if n_args = 0
            for key, value in kwargs.items():
                exec("self.{} = {}".format(key, value))
