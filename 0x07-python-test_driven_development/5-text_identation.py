#!/usr/bin/python3
"""module for function thats print text with replaces"""


def text_identation(text):
    """new lines after ., ? or :"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    a = text.replace(". ", "\n\n")
    b = text.repalce(": ", ":\n\n")
    c = text.replace("? ", "?\n\n")
    print(c, end="")
