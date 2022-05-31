#!/usr/bin/python3
"""function that adds attributes to an object"""


def add_attribute(obj, name, value):
    if type(name) is not str:
        raise TypeError("can't add new attribute")
    try:
        exec("obj.{} = value".format(name))
    except:
        raise TypeError("can't add new attribute")
