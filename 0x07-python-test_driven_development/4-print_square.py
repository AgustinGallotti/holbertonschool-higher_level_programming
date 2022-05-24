#!/usr/bin/python3
"""module of a function to print a square"""

def print_square(size):
    """print a square with #"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    string = '#' * size
    for i in range(size):
        print(string)
