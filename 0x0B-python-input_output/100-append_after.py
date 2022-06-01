#!/usr/bin/python3
"""function that insert a line of text to a file, after each line
   containing a specific string"""


def append_after(filename="", search_string="", new_string=""):
    """defined to append"""
    with open(filename, "r+") as listt:
        reading = listt.readlines()
        listt.seek(0)
        for i in reading:
            if search_string in i:
                listt.write(new_string)
            listt.write(i)
        listt.truncate()
