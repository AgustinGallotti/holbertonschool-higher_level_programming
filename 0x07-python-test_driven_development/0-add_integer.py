#!/usr/bin/python3
"""
    module
"""
def add_integer(a, b=98):
    """ Adds to nubmers as integers"""
    if type(a) is not float or type(a) is not int:
        TypeError("a must be an integer")
    if type(b) is not float or type(b) is not int:
        TypeError("b must be an integer")

    return int(a) + int(b)
