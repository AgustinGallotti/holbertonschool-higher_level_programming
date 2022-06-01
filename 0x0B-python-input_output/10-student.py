#!/usr/bin/python3
"""define class student"""


class Student:
    """class"""
    def __init__(self, first_name, last_name, age):
        """define my id"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """return info"""
        if attrs is not None:
            return {key: value for key,
                    value in self__dict__.items() if key in attrs}
        else:
            return self.__dict__
