#!/usr/bin/python3
"""function that prints n number of lines from a file"""


def append_write(filename="", text=""):
    """built for append"""
    with open(filename, mode="a", encoding="UTF-8") as f:
        return f.write(text)
