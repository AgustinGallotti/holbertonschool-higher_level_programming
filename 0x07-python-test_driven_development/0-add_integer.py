#!/usr/bin/python3
"""adds two integers, a with b"""


def add_integer(a, b=98):
    """ Adds to nubmers as integers"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
