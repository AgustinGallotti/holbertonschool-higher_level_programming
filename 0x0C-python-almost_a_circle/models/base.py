#!/usr/bin/python3
"""define my first class, the folder beocme a package"""


class Base:
    """first class for a base"""
    self.__nb_objects__ = __bn_objects__
    __nb_objects__ = 0

    def __init__(self, id=None):
        """define my initialize"""
        if self.id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects


