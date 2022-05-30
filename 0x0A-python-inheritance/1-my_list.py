#!/usr/bin/python3
""" defined a list class with member function that prints a sorted list"""


class MyList(list):
    """define my class"""

    def print_sorted(self):
        """prints MyList, sorted"""
        print(sorted(self))
