#!/usr/bin/python3
"""function that adds attributes to an object"""


def add_attribute(obj, name, value):
    """defined my obj"""
    if hasattr(obj) and not hasattr(obj, att):
        """The method hasattr, return true if an obj has the given named attr
        or false if it does not"""
        raise TypeError("can't add new attribute")
    if not hasattr(obj) and not hasattr(obj, __slots__):
        """Concept of memory optimisation on objects,
        __slots__, reduce the size of objects"""
        raise TypeError("can't add new attribute")

    setattr(obj, att, value)
