#!/usr/bin/python3
"""funtion that prints the number of lines in a UTF-8 text file"""


def append_write(filename="", text=""):
    with open(filename, "w") as f:
        filename.writelines(text)
        filename.close()
