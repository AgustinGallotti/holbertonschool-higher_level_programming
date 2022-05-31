#!/usr/bin/python3
"""function that prints n number of lines from a file"""


def append_write(filename="", text=""):
    with open(filename, mode="a", encoding="utf=8") as f:
        return f.write(text)
