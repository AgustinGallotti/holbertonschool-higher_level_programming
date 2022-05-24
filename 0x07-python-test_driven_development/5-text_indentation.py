#!/usr/bin/python3
"""module for function thats print text with replaces"""


def text_indentation(text):
    """new lines after ., ? or :"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    a = text.replace(". ", ".\n\n")
    b = a.replace(": ", ":\n\n")
    c = b.replace("? ", "?\n\n")
    print(c, end="")
