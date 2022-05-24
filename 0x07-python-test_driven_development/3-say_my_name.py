#!/usr/bin/python3
"""module for function that print two strings"""
def say_my_name(first_name, last_name=""):
    """Prints as name"""
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("laste_name must be a string")
    print("My name is", first_name, last_name)
