#!/usr/bin/python3
"""function that prints a UTF-8 text file"""


def read_file(filename=""):
    """defined my built"""
    with open(filename, "r", encoding="UTF-8") as f:
        print(f.read(), end="")
