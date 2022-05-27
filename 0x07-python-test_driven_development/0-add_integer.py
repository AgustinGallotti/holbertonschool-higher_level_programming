#!/usr/bin/python3
"""adds two integers, a with b"""


def add_integer(a, b=98):
    """ Adds to nubmers as integers"""
    if isinstance(a, float) or isinstance(b, float):
        a = int(a)
        b = int(b)

    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    elif not isinstance(b, int):
        raise TypeError("b must be an integer")

    return a + b
