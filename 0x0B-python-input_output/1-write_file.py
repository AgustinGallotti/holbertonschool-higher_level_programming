#!/usr/bin/python3
"""funtion that prints the number of lines in a UTF-8 text file"""


def write_file(filename="", text=""):
    with open(filename, "w") as f:
        return (f.write(text))
