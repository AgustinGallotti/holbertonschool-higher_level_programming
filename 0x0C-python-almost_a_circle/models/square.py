#!/usr/bin/python3
"""square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """define my square"""
    def __init__(self, size, x=0, y=0, id=None):
        """intialize"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """print"""
        return "[Square] ({}) {}/{} - {}".\
            format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """size"""
        return self.width

    @size.setter
    def size(self, size):
        """size replace"""
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """positional order"""
        n_args = len(args)
        if n_args > 0:
            self.id = args[0]
        if n_args > 1:
            self.width = args[1]
            self.height = args[1]
        if n_args > 2:
            self.x = args[2]
        if n_args > 3:
            self.y = args[3]
        if n_args == 0:
            for key, value in kwargs.items():
                exec("self.{} = {}".format(key, value))

    def to_dictionary(self):
        """return an dicitonary"""
        n_dict = {"id": self.id, "size": self.width,
                  "x": self.x, "y": self.y}
        return n_dict
