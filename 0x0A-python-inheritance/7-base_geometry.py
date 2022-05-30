#!/usr/bin/python3
"""define thebase geometry class"""


class BaseGeometry:
    """baseclass for geometry objects"""

    def area(self):
        """return area of geometry objects"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate whether values is an integer"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
