#!/usr/bin/python3
"""
    module
"""
def say_my_name(first_name, last_name=""):
    if first_name is not str:
        raise TypeError("first_name must be a string")
    if last_name is not str:
        raise TypeError("laste_name must be a string")
